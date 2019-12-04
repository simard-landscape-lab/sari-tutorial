# SARI-Tutorial

Conference [link](http://sari.umd.edu/meetings/international-regional-science-training).

These tutorials are educational materials for a 3-hour tutorial at the above conference. The material is collected across public data and material that is taught in universities and can be readily found in textbooks.

## Installation Instructions


I tested this on Mac 10.14 using the anaconda [distribution](https://www.anaconda.com/distribution/). Different OS's will likely require some reconfiguration.

1. Download repository
2. create a virtual environment - preferably using conda via: `conda create --name sari_tutorial python=3.7`
3. Activate virtual environment - with conda that is: `conda activate sari_tutorial`.
4. Change working directory to this repository and `pip install -r requirements.txt`
5. Create a new jupyter kernel using `python -m ipykernel install --user --name sari_tutorial`

When running notebooks, make sure you are using the kernel `sari_tutorial`.

# Acknowledgements

We gratefully and humbly acknowledge JAXA for the use of a coherence image over Gabon generated using ISCE2.

A portion of this research was performed at the Jet Propulsion Laboratory, California Institute of Technology. Copyright 2019 California Institute of Technology. US Government Support Acknowledged.
