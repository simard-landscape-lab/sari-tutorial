# SARI-Tutorial

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cmarshak/sari-tutorial/master)


This tutorial was given at [SARI](http://sari.umd.edu/) training [conference](http://sari.umd.edu/meetings/international-regional-science-training) associated with NASA's [LCLUC program](https://lcluc.umd.edu/). This tutorial was written by Charlie Marshak and supervised by [Marc Simard](https://scholar.google.com/citations?user=JQJF1wgAAAAJ&hl=en).

These tutorials are educational materials for a 3-hour tutorial at the above conference. The material is collected across public data and open source software. Much of the content can be readily found in university textbooks and is taken directly from open source software documentation and online forums, which we acknowledge wherever possible. There are exercises, most of which are very minor modifications of the demonstrations.


## Installation Instructions

These are the routes we took to get this tutorial working on a Mac and Windows machine. Of course, these are but suggestions and the user is invited to install the various requirements as they wish. Further, these installations will need to be updated as distributions change (last updated: December 2019).

### Mac

I tested this on Mac 10.14 using the anaconda distribution. Download the anaconda distribution [here](https://www.anaconda.com/distribution/) and follow the instructions (we selected the default options when prompted during installation). After you have successfully downloaded python, do the following:

1. Download the repository.
2. Open the [terminal](https://support.apple.com/guide/terminal/welcome/mac).
3. Change the working directory of the terminal session to the downloaded repository.
4. Create a virtual environment using conda via: 

	`conda create --name sari_tutorial python=3.7`
	
	Make sure to hit `y` to confirm that the listed packages can be downloaded for this environment.

5. Activate the virtual environment: 

	`conda activate sari_tutorial`.

6. Install requirements: 

	`pip install -r requirements.txt`

7. Create a new jupyter kernel: 

	`python -m ipykernel install --user --name sari_tutorial`.

When running notebooks, make sure you are using the kernel `sari_tutorial`.


### Windows

I tested this on Windows 10 using the anaconda distribution. Download the anaconda distribution [here](https://www.anaconda.com/distribution/) and follow the instructions (we selected the default options when prompted during installation). After you have successfully downloaded python, do the following:

1. Download repository.
2. Open the [anaconda prompt application](https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-prompt-win), which will have been downloaded if you used the Anaconda distribution above.
3. Change the working directory of the prompt session to this repository.
4. Create a virtual environment with conda: 
	
	`conda create --name sari_tutorial python=3.7`
	
	Make sure to hit `y` to confirm that the listed packages can be downloaded for this environment.

4. Activate the virtual environment: 
	
	`conda activate sari_tutorial`

6.  Install window requirements with conda: 
	
	`conda install -c conda-forge --yes --file requirements_windows.txt`

7. Install geopy with `pip`:
	
	`pip install geopy`
	
8. Create a new jupyter kernel: 
	
	`python -m ipykernel install --user --name sari_tutorial`

## Usage with QGIS

QGIS is an open-source viewer for geo-referenced rasters.

Please download the application [here](https://www.qgis.org/en/site/) and follow the instructions found therein. Once downloaded, drag one of the tifs in the `data` folder of this repository and explore. We will frequently save products as geo-referenced rasters so viewing them in detail is very important.

## Usage with Jupyter

If you installed python using the Anaconda distribution, `jupyter` is already installed!

Using the terminal (for Mac) or Anaconda prompt (for Windows) - navigate to the current working directory of this repository and launch a jupyter notebook with the command: `jupyter-notebook`. Your internet browser should open and you can now open `*.ipynb` files in each of the training modules e.g. `2_GIS/2_GIS.ipynb`. There are many instructional videos on youtube and elsewhere on how to use jupyter-notebooks including this short [one](https://www.codecademy.com/articles/how-to-use-jupyter-notebooks) from code-academy.

When running notebooks, make sure you are using the kernel `sari_tutorial`, which will be an available kernel if you followed the installation instructions above. You can select the kernel `sari_tutorial` in the menu as illustrated in the screenshot below (`sari_tutorial` will be listed in the menu where `Python 2` is).

![screenshot](https://i.stack.imgur.com/F0Cbi.png)
*The image is from Stackoverflow*.

# Acknowledgements

This tutorial was written by Charlie Marshak and supervised closely by [Marc Simard](https://scholar.google.com/citations?user=JQJF1wgAAAAJ&hl=en). 

This tutorial was for the 2019 SARI training [conference](http://sari.umd.edu/meetings/international-regional-science-training) held at Prince of Songkla University, Phuket Campus. We are grateful to the conference organizers (in particular [Krishna Vadrevu](https://geog.umd.edu/facultyprofile/vadrevu/krishna)), the [SARI program](http://sari.umd.edu/), and the [LCLUC program](https://lcluc.umd.edu/) working to make this training conference possible. We are grateful for the input from and helpful conversations with [Michael Denbina](https://www.researchgate.net/profile/Michael_Denbina), [Tien-Hao Liao](https://scienceandtechnology.jpl.nasa.gov/tien-hao-liao), and Neda Kasraee. 

We gratefully and humbly acknowledge JAXA for the use of ALOS-2 data to generate a coherence image over Mondah, Gabon generated using ISCE2. We are also grateful to the ASF for providing easy access to ALOS-1 radiometrically and terrain corrected tiles over Mondah and Ko Panyi.

A portion of this research was performed at the Jet Propulsion Laboratory, California Institute of Technology. Copyright 2019 California Institute of Technology. US Government Support Acknowledged.