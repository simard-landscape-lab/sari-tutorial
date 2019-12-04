# Downloading Data

*All the data in this tutorial has been downloaded for you. This page is a reference of some websites/open source tools/etc. We gratefully and humbly acknowledge JAXA for the use of a coherence image over Gabon generated using ISCE2.* 

We will reference image repositories throughout the tutorial wherever applicable. In this tutorial, we concentrate on images from the L-band SAR sensor from [ALOS/PALSAR](https://global.jaxa.jp/projects/sat/alos/). L-band sensors are popular for forest analysis due to their long wavelengths and ability to penetrate canopy cover for additional information. ALOS-1 was a satellite that was active from 2007-2010 that had the L-band PALSAR-1 sensor and ALOS-2 is its successor with the PALSAR-2 sensor. There are numerous other satellite SAR sensors including Sentinel-1 (C-band) and UAVSAR (airborne L-band).

This list below was made relatively quickly. Hope this gets you started. Most of the links will direct you to NASA operated data repository, which are open but require a login. New users can register [here](https://urs.earthdata.nasa.gov/users/new).

# SAR

## ALOS-1

All the products below are for [backscatter](http://ceos.org/document_management/SEO/DataCube/Laymans_SAR_Interpretation_Guide_2.0.pdf) images that have been [radiometrically terrain corrected](http://www.geo.uzh.ch/microsite/rsl-documents/research/publications/peer-reviewed-articles/201108-TGRS-Small-tcGamma-3809999360/201108-TGRS-Small-tcGamma.pdf).

1. Alaska Site Facility
	+ [Vertex](https://vertex.daac.asf.alaska.edu/)
	+ [HyP3](http://hyp3.asf.alaska.edu/) 
		- this tools actually makes it easy for you to obtain coherence images (derived from pairs), interferograms, etc.
		- To do one-time processing of a site, you have to contact the ASF - you have monthly quotas.

2. JAXA [Mosaics](https://www.eorc.jaxa.jp/ALOS/en/palsar_fnf/fnf_index.htm). You have to register first and then downloading is free. This provides global annual RTC mosaics at 25 m scale! *Warning*: known geocoding issues that appear has pixel/half-pixel shifts from year to year or when comparing to other SAR images.

## ALOS-2

This is currently not open - we do not provide raw data that you would download - only the coherence product obtained via ISCE2.

However, there is a recently announced [agreement](https://www.earthobservations.org/article.php?id=392) so that a large portion of the radar data can be made public. 

I want to emphasize how important (and exciting, at least for SAR) this is for forest monitoring and biomass analysis. L-band is extremely powerful for forest studies because it is able to penetrate the canopy. Additionally, the short repeat pass time of ALOS-2 (14 days!) makes a lot of the interferometric products equally interesting and valuable for large and insightful studies, even with zero-spatial baseline. We are truly grateful to JAXA for providing Simard's lab access to this data for large regional studies.

## UAVSAR

1. [UAVSAR data](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl).
	+ "Stacks" are for inteferograms 
		- can process using the python library [Kapok](https://github.com/mdenbina/kapok) - here is an excellent Kapok [tutorial](https://github.com/mdenbina/kapok/blob/master/docs/manual.pdf). 
		- ISCE2 can also process these stacks using there insarApp framework. Here is the related `xml` [file](https://github.com/isce-framework/isce2/blob/da9a8afaf593e386cfe55a5495c59e2141481794/examples/input_files/isceappUAVSAR_Stack.xml) - see more on ISCE2 below.
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

## ISCE2

[ISCE2](https://github.com/isce-framework/isce2) is for SAR interferometry. We using some interferometric products, but the full range of what can be done is quite astounding just with this software e.g. geological deformation within centimeters of accuracy. There are also tons of tools that build on the products that use ISCE2 generates such as [mintpy](https://github.com/insarlab/MintPy), but this is not relevant for this tutorial.

We used ISCE2 to process Alos-2 coherence data over Gabon. We note for mac and linux that there is a [conda install](https://anaconda.org/conda-forge/isce2)! That means you can make your virtual environment and then install ISCE2 - the previous install instructions are atrocious.

If you are interested in learning more, here are some [notebooks](https://github.com/isce-framework/isce2-docs/tree/master/Notebooks) illustrating ISCE2 use cases for various SAR sensors including how to generate interferograms and coherence from ALOS-1 [here](https://github.com/isce-framework/isce2-docs/blob/master/Notebooks/Stripmap/stripmapApp.ipynb).

## SNAP

[SNAP](https://step.esa.int/main/toolboxes/snap/) is meant to process all Sentinel data. This includes RTC-ing SAR images - fortunately, it read not just from Sentinel data. This excellent, detailed [tutorial](https://gis1.servirglobal.net/TrainingMaterials/SAR/chp6_training_E.pdf) by Dr. Marc Simard details how to RTC SAR images, which is highly relevant for using the tools discussed in this tutorial should an RTC image not be directly available.

## QGIS

[QGIS](https://www.qgis.org/en/site/) is a great open-source raster/vector viewer. Get to know it!

## Google Earth Engine

Very powerful tool for obtaining remote sensing images, many of them processed and ready for analysis.

Here are some nice [jupyter](https://github.com/tylere/agu2017) from AGU 2017 and related [video](https://www.youtube.com/watch?v=LzxQH0Ze0iI&feature=youtu.be&t=19m54s) resources from Tyler Erickson. There are tons of [examples](https://github.com/google/earthengine-api/tree/master/python/examples) on the earth engine github as well.