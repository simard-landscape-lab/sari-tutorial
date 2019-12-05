# SARI-Tutorial

Conference [link](http://sari.umd.edu/meetings/international-regional-science-training).

These tutorials are educational materials for a 3-hour tutorial at the above conference. The material is collected across public data and material that is taught in universities and can be readily found in textbooks.

## Installation Instructions

These are the routes we took to install this successfully on our computer - of course, the user is invited to install how they wish.

### Mac

I tested this on Mac 10.14 in December 2019 using the anaconda [distribution](https://www.anaconda.com/distribution/).

1. Download the repository.
2. Open the [terminal](https://support.apple.com/guide/terminal/welcome/mac).
3. Change the working directory of the terminal session to this repository.
4. Create a virtual environment using conda via: 

	`conda create --name sari_tutorial python=3.7`

5. Activate the virtual environment: 

	`conda activate sari_tutorial`.

6. Install requirements: 

	`pip install -r requirements.txt`

7. Create a new jupyter kernel: 

	`python -m ipykernel install --user --name sari_tutorial`.

When running notebooks, make sure you are using the kernel `sari_tutorial`.


### Windows

I tested this on Windows 10 in December 2019 using the anaconda [distribution](https://www.anaconda.com/distribution/).

1. Download repository.
2. Open the [anaconda prompt application](https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-prompt-win).
3. Change the working directory of the prompt session to this repository.
4. Create virtual environment with conda: 
	`conda create --name sari_tutorial python=3.7`

4. Activate the virtual environment: 
	
	`conda activate sari_tutorial`

6.  Install window requirements with conda: 
	
	`conda install -c conda-forge --yes --file requirements_windows.txt`

7. Install geopy with `pip`:
	
	`pip install geopy`
	
8. Create a new jupyter kernel: 
	
	`python -m ipykernel install --user --name sari_tutorial`

When running notebooks, make sure you are using the kernel `sari_tutorial`.


# Acknowledgements

We gratefully and humbly acknowledge JAXA for the use of ALOS-2 data to generate a coherence image over Mondah, Gabon generated using ISCE2.

A portion of this research was performed at the Jet Propulsion Laboratory, California Institute of Technology. Copyright 2019 California Institute of Technology. US Government Support Acknowledged.
