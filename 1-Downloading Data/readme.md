# Downloading Data

*All the data in this tutorial has been downloaded for you. This page is a reference of some sites/tools/etc for larger scale use.* 

We will reference image repositories throughout the tutorial wherever applicable.

In this tutorial, we will concentrate on images from the L-band SAR sensor from [ALOS/PALSAR-1](https://global.jaxa.jp/projects/sat/alos/). ALOS-1 is a satellite that was active from 2007-2010 that had the L-band PALSAR-1 sensor. There are numerous other sattelite SAR sensors including Sentinel-1 (C-band), ALOS-2 (L-band), and UAVSAR (L-band). L-band sensors are popular for forest analysis due to their long wavelengths and ability to penetrate canopy cover for additional information.

This list was made relatively quickly, so will be updated periodically. Hope this gets you started.

# SAR

## ALOS-1

All the products below are for [backscatter](http://ceos.org/document_management/SEO/DataCube/Laymans_SAR_Interpretation_Guide_2.0.pdf) images that have been [radiometrically terrain corrected](http://www.geo.uzh.ch/microsite/rsl-documents/research/publications/peer-reviewed-articles/201108-TGRS-Small-tcGamma-3809999360/201108-TGRS-Small-tcGamma.pdf).

1. Alaska Site Facility
	+ [Vertex](https://vertex.daac.asf.alaska.edu/)
	+ [HyP3](http://hyp3.asf.alaska.edu/) - this tools actually makes it easy for you to obtain coherence images (derived from pairs), interferograms, etc.

2. JAXA [Mosaics](https://www.eorc.jaxa.jp/ALOS/en/palsar_fnf/fnf_index.htm). You have to register first and then downloading is free. *Warning*: known geocoding issues that appear has pixel/half-pixel shifts.

## UAVSAR

1. [UAVSAR data](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl).
	+ "Stacks" are for inteferograms - can process using [Kapok](https://github.com/mdenbina/kapok) - here is an excellent [tutorial](https://github.com/mdenbina/kapok/blob/master/docs/manual.pdf). ISCE2 can also process these stacks using there insarApp framework. Here is the related `xml` [file](https://github.com/isce-framework/isce2/blob/da9a8afaf593e386cfe55a5495c59e2141481794/examples/input_files/isceappUAVSAR_Stack.xml).
	+ "PolSAR" data is for backscatter analysis and decompositions. Must be RTC-ed. [HyP3](http://hyp3.asf.alaska.edu/) allows you to process this using the proprietary software gamma.
2. Marc Simard's UAVSAR [data](https://landscape.jpl.nasa.gov/) over Boreal forest in the Laurentides that has been processed can be dowloaded.

## Sentinel-1

1. ESA's [OpenHub](https://scihub.copernicus.eu/)
2. Alaska Site Facility [Vertex](https://vertex.daac.asf.alaska.edu/)
3. AWS Repo and related viewers (might cost $$ to request/download data) found [here](https://registry.opendata.aws/sentinel-1/).

# Optical

	
## Landsat

1. [Earth Explorer](https://earthexplorer.usgs.gov/)
2. Hansen Mosaics for Forest Analyses - first and last images are very useful.
	+ [Mosaics](https://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.6.html)


# Processing Tools

## SNAP

[SNAP](https://step.esa.int/main/toolboxes/snap/) is meant to process all Sentinel data. This includes RTC-ing SAR images - fortunately, it read not just from Sentinel data. This excellent, detailed [tutorial](https://gis1.servirglobal.net/TrainingMaterials/SAR/chp6_training_E.pdf) by Dr. Marc Simard details how to RTC SAR images, which is highly relevant for using the tools discussed in this tutorial should an RTC image not be directly available.

## QGIS

[QGIS](https://www.qgis.org/en/site/) is a great open-source raster/vector viewer. Get to know it!

## Google Earth Engine

Very powerful tool for obtaining remote sensing images, many of them processed and ready for analysis.

Here are some nice [jupyter]((https://github.com/tylere/agu2017) from AGU 2017 and related [video](https://www.youtube.com/watch?v=LzxQH0Ze0iI&feature=youtu.be&t=19m54s) resources from Tyler Erickson. There are tons of [examples](https://github.com/google/earthengine-api/tree/master/python/examples) on the earth engine github as well.