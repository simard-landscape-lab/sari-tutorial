# SARI-Tutorial

Conference [link](http://sari.umd.edu/meetings/international-regional-science-training).

These tutorials are educational materials for a 3-hour tutorial at the above conference. The material is collected across public data and material that is taught in universities and can be readily found in textbooks.

## Installation Instructions

These are the routes we took to install this successfully various local machines - of course, the user is invited to install how they wish and will need to be updated as distributions change (last updated: December 2019).

### Mac

I tested this on Mac 10.14 using the anaconda distribution. Download [here](https://www.anaconda.com/distribution/) and follow the instructions. After you have successfully downloaded python, do the following:

1. Download the repository.
2. Open the [terminal](https://support.apple.com/guide/terminal/welcome/mac).
3. Change the working directory of the terminal session to the downloaded repository.
4. Create a virtual environment using conda via: 

	`conda create --name sari_tutorial python=3.7`
	
	Make sure to hit `y` to confirm the listed packages that will be downloaded for this environment.

5. Activate the virtual environment: 

	`conda activate sari_tutorial`.

6. Install requirements: 

	`pip install -r requirements.txt`

7. Create a new jupyter kernel: 

	`python -m ipykernel install --user --name sari_tutorial`.

When running notebooks, make sure you are using the kernel `sari_tutorial`.


### Windows

I tested this on Windows 10 using the anaconda distribution. Download [here](https://www.anaconda.com/distribution/) and follow the instructions. After you have successfully downloaded python, do the following:

1. Download repository.
2. Open the [anaconda prompt application](https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-prompt-win), which will have been downloaded if you used the Anaconda distribution above.
3. Change the working directory of the prompt session to this repository.
4. Create a virtual environment with conda: 
	
	`conda create --name sari_tutorial python=3.7`
	
	Make sure to hit `y` to confirm the listed packages that will be downloaded for this environment.

4. Activate the virtual environment: 
	
	`conda activate sari_tutorial`

6.  Install window requirements with conda: 
	
	`conda install -c conda-forge --yes --file requirements_windows.txt`

7. Install geopy with `pip`:
	
	`pip install geopy`
	
8. Create a new jupyter kernel: 
	
	`python -m ipykernel install --user --name sari_tutorial`


## Usage with Jupyter

If you installed python using the Anaconda distribution, `jupyter` is already installed!

Using the terminal (for Mac) or Anaconda prompt (for Windows) - navigate to the current working directory of this repository and launch a jupyter notebook with the command: `jupyter-notebook`. Your internet browser should open and you can now open `*.ipynb` files in each of the training modules e.g. `2_GIS/2_GIS.ipynb`. There are many instructional videos on youtube and elsewhere on how to use jupyter-notebooks including this short [one](https://www.codecademy.com/articles/how-to-use-jupyter-notebooks) from code-academy.

When running notebooks, make sure you are using the kernel `sari_tutorial`, which will be an available kernel if you followed the installation instructions above. You can select the kernel `sari_tutorial` in the menu as illustrated in the screenshot below (`sari_tutorial` will be listed not just `Python 2`).

![screenshot](https://i.stack.imgur.com/F0Cbi.png)

# Acknowledgements

We gratefully and humbly acknowledge JAXA for the use of ALOS-2 data to generate a coherence image over Mondah, Gabon generated using ISCE2.

A portion of this research was performed at the Jet Propulsion Laboratory, California Institute of Technology. Copyright 2019 California Institute of Technology. US Government Support Acknowledged.
