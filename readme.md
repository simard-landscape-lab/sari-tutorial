# SARI-Tutorial

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cmarshak/sari-tutorial/master)


These tutorial materials are for [SARI](http://sari.umd.edu/) training and webinars associated with NASA's [LCLUC program](https://lcluc.umd.edu/). These tutorials are designed by Charlie Marshak and [Marc Simard](https://scholar.google.com/citations?user=JQJF1wgAAAAJ&hl=en).

These tutorials are educational materials for SARI conference and webinars. The material is collected across public data and open source software. Much of the content can be readily found in university textbooks and is taken directly from open source software documentation and online forums, which we acknowledge wherever possible. 

## Update

We updated this repository so that it reflects the webinar hosted April 16, 2020.

The Phuket training can still be found under the branch `sari-phuket-2019`.


## Installation Instructions

These are the routes we took to get this tutorial working on a Mac and Windows machine. Of course, these are but suggestions and the user is invited to install the various requirements as they wish. Further, these installations will need to be updated as distributions change.

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
	
7. Create a new jupyter kernel: 
	
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

This tutorial was written by Charlie Marshak and [Marc Simard](https://scholar.google.com/citations?user=JQJF1wgAAAAJ&hl=en). 

We are grateful to the SARI researchers [Krishna Vadrevu](https://geog.umd.edu/facultyprofile/vadrevu/krishna) and [Werapong Koedsin](http://werapong-g.space.psu.ac.th/). We also thank the [SARI](http://sari.umd.edu/) and [LCLUC](https://lcluc.umd.edu/) programs, especially [Garik Gutman](https://lcluc.umd.edu/people/garik-gutman), making such trainings/webinars possible. We are grateful for the input from and helpful conversations with [Michael Denbina](https://www.researchgate.net/profile/Michael_Denbina), [Tien-Hao Liao](https://scienceandtechnology.jpl.nasa.gov/tien-hao-liao), and Neda Kasraee. 

We gratefully and humbly acknowledge JAXA for the use of ALOS-1/-2 data in addition to ASF for providing easy access to high resolution ALOS-1 data.

A portion of this research was performed at the Jet Propulsion Laboratory, California Institute of Technology. 

Copyright 2020 by the California Institute of Technology. ALL RIGHTS RESERVED. United States Government Sponsorship acknowledged. Any commercial use must be negotiated with the Office of Technology Transfer at the California Institute of Technology.

This software may be subject to U.S. export control laws. By accepting this software, the user agrees to comply with all applicable U.S. export laws and regulations. User has the responsibility to obtain export licenses, or other export authority as may be required before exporting such information to foreign countries or providing access to foreign persons.