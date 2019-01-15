# Paparazzi
Paparazzi: Surface Editing by way of Multi-view Image Processing

### Modular version
We have two versions available: one with a "Matlab-esque" main loop in the ```master``` branch and a a more [modular version](https://github.com/HTDerekLiu/Paparazzi/tree/modular) in the ```modular``` branch that separates separates components of our main loop.
The modular branch can be installed with ```pip```:
```bash
pip2 install git+https://github.com/HTDerekLiu/Paparazzi.git@modular
```

### Fetching the repo
Please remember to pull the submodules for this repository:
```bash
git submodule update --init --recursive
```

#### Setup
Paparazzi is tested on Ubuntu 16.04 machine on python 2.7. Dependencies include Eigen, BLAS, LAPACK, PyOpenGL, and PyGLFW. One option to install the dependencies is to run
```
conda install python=2.7 cmake gcc
conda install -c omnia eigen3
conda install -c conda-forge blas
conda install -c menpo glfw3
pip install pyopengl pyglfw scikit-image pyeltopo
```

Alternatively it can be run in a docker by:
```
sh dockerbuild.sh
sh dockerrun.sh
```

#### Bibtex
```
@article{Liu:Paparazzi:2018,
  title = {Paparazzi: Surface Editing by way of Multi-View Image Processing},
  author = {Hsueh-Ti Derek Liu and Michael Tao and Alec Jacobson},
  year = {2018},
  journal = {ACM Transactions on Graphics}, 
}
```
