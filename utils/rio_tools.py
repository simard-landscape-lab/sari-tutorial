from rasterio.warp import calculate_default_transform, reproject, Resampling, aligned_target
from rasterio.transform import xy
from affine import Affine
from rasterio import features
from rasterio.features import shapes
import numpy as np
import fiona
from geopy import distance
import pyproj


def polygonize_array_to_shapefile(arr, profile, shape_file_dir, label_name='label', mask=None):

    if mask is None:
        mask = np.ones(arr.shape).astype(bool)
    else:
        # mask is data mask
        mask = ~mask.astype(bool)

    dtype = str(arr.dtype)
    if 'int' in dtype or 'bool' in dtype:
        arr = arr.astype('int32')
        dtype = 'int32'
        dtype_for_shape_file = 'int'

    if 'float' in dtype:
        arr = arr.astype('float32')
        dtype = 'float32'
        dtype_for_shape_file = 'float'

    transform = profile['transform']
    crs = profile['crs']
    features = list(shapes(arr, mask=mask, transform=transform))
    results = list({'properties': {label_name: (value)}, 'geometry': geometry} for i, (geometry, value) in enumerate(features))
    with fiona.open(shape_file_dir, 'w',
                    driver='ESRI Shapefile',
                    crs=crs,
                    schema={'properties': [(label_name, dtype_for_shape_file)],
                            'geometry': 'Polygon'}) as dst:
        dst.writerecords(results)


def rasterize_shapes_to_array(shapes: list,
                              attributes: list,
                              profile: dict,
                              all_touched=False,
                              fill_value=0):

    """
    Rasterizers a list of shapes and burns them into array with given attributes.

    Nodata from profile will be used as fill value.
    """
    out_arr = np.ones((profile['height'], profile['width']), dtype=profile['dtype'])
    out_arr = out_arr * fill_value


    # this is where we create a generator of geom, value pairs to use in rasterizing
    shapes = [(geom, value) for geom, value in zip(shapes, attributes)]
    burned = features.rasterize(shapes=shapes,
                                out=out_arr,
                                fill=fill_value,
                                transform=profile['transform'],
                                all_touched=all_touched)

    return burned


def reproject_arr_to_match_profile(src_array: np.ndarray,
                                   src_profile: dict,
                                   ref_profile: dict,
                                   nodata=None,
                                   resampling='bilinear'):
    height, width = ref_profile['height'], ref_profile['width']
    crs = ref_profile['crs']
    transform = ref_profile['transform']
    count = src_profile['count']

    src_dtype = src_profile['dtype']

    reproject_profile = ref_profile.copy()
    reproject_profile.update({'dtype': src_dtype})

    if nodata is None:
        nodata = src_profile['nodata']
    reproject_profile.update({'nodata': nodata,
                              'count': count})

    dst_array = np.zeros((count, height, width))

    resampling = Resampling[resampling]

    reproject(src_array,
              dst_array,
              src_transform=src_profile['transform'],
              src_crs=src_profile['crs'],
              dst_transform=transform,
              dst_crs=crs,
              dst_nodata=nodata,
              resampling=resampling)
    return dst_array.astype(src_dtype), reproject_profile


def get_cropped_profile(profile: dict, slice_x: slice, slice_y: slice):
    """
    slice_x and slice_y are numpy slices
    """
    x_start = slice_x.start or 0
    y_start = slice_y.start or 0
    x_stop = slice_x.stop or profile['width']
    y_stop = slice_y.stop or profile['height']

    width = x_stop - x_start
    height = y_stop - y_start

    profile_cropped = profile.copy()

    trans = profile['transform']
    x_cropped, y_cropped = xy(trans, y_start, x_start, offset='ul')
    trans_list = list(trans.to_gdal())
    trans_list[0] = x_cropped
    trans_list[3] = y_cropped
    tranform_cropped = Affine.from_gdal(*trans_list)
    profile_cropped['transform'] = tranform_cropped

    profile_cropped['height'] = height
    profile_cropped['width'] = width

    return profile_cropped


def get_bounds_dict(profile):
    lx, ly = profile['width'], profile['height']
    transform = profile['transform']
    bounds_dict = {'left': transform.c,
                   'right': transform.c + transform.a * lx,
                   'top': transform.f,
                   'bottom': transform.f + transform.e * ly
                   }
    return bounds_dict


def reproject_profile_to_new_crs(src_profile,
                                 dst_crs,
                                 resolution=None):
    reprojected_profile = src_profile.copy()
    bounds_dict = get_bounds_dict(src_profile)

    src_crs = src_profile['crs']
    dst_transform, dst_width, dst_height = calculate_default_transform(src_crs,
                                                                       dst_crs,
                                                                       src_profile['width'],
                                                                       src_profile['height'],
                                                                       **bounds_dict
                                                                       )

    if resolution is not None:
        dst_transform, dst_width, dst_height = aligned_target(dst_transform, dst_width, dst_height, resolution)
    reprojected_profile.update({
                                'crs': dst_crs,
                                'transform': dst_transform,
                                'width': dst_width,
                                'height': dst_height,
                                })
    return reprojected_profile


def reproject_arr_to_new_crs(src_array,
                             src_profile,
                             dst_crs,
                             resampling='bilinear',
                             resolution=None):
    reprojected_profile = reproject_profile_to_new_crs(src_profile, dst_crs, resolution=resolution)
    resampling = Resampling[resampling]
    dst_array = np.zeros((reprojected_profile['count'], reprojected_profile['height'], reprojected_profile['width']))

    reproject(
              # Source parameters
              source=src_array,
              src_crs=src_profile['crs'],
              src_transform=src_profile['transform'],
              # Destination paramaters
              destination=dst_array,
              dst_transform=reprojected_profile['transform'],
              dst_crs=reprojected_profile['crs'],
              dst_nodata=src_profile['nodata'],
              # Configuration
              resampling=resampling,
              )
    return dst_array, reprojected_profile
