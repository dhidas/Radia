# Radia
3D Magnetostatics Computer Code


## Building on apcpu
make clean
make all

### Python
module load python/3.7
make
cd cpp/py
python setup.py install --user # remove the --user for system install

### Mathlink (mathematica)
cd cpp/gcc
make -f Makefile_intermed


# Notes
Edit cpp/gcc/Makefile(s) to change mathematica versions, etc
