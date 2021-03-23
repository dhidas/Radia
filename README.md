# Radia
3D Magnetostatics Computer Code


## Building on cluster
```
make clean
MODE=mpi make all
```

### Python
```
cd cpp/py
MODE=mpi python setup.py install --user
```

### Mathlink (mathematica)
```
cd cpp/gcc
make -f Makefile_intermed
```

# Notes
Edit cpp/gcc/Makefile(s) to change mathematica versions, etc
