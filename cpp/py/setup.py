from setuptools import setup, Extension
import os


ext_kwargs = {
    'define_macros': [('MAJOR_VERSION', '1'), ('MINOR_VERSION', '0')],
    'include_dirs': [
        os.path.abspath('../src/lib'),
        os.path.abspath('../src/ext/auxparse'),
        os.path.abspath('../src/core'),
        ],
    'libraries': ['radia', 'm', 'fftw'],
    'library_dirs': [
        os.path.abspath('../gcc'),
        os.path.abspath('../../ext_lib'),
        ],
    'sources': [os.path.abspath('../src/clients/python/radpy.cpp')]
    } 

if 'MODE' in os.environ: 
    sMode = str(os.environ['MODE'])
    if sMode == 'mpi': 
        ext_kwargs.update({
            'include_dirs': [
                os.path.abspath('../src/lib'),
                os.path.abspath('../src/ext/auxparse'),
                os.path.abspath('../src/core'),
                os.path.abspath('/usr/lib/openmpi/include'),
                os.path.abspath(os.environ['MPI_INCLUDE']),
                ],
            'libraries': ['radia', 'm', 'fftw', 'mpicxx', 'dl'],
            'library_dirs': [
                os.path.abspath('../gcc'),
                os.path.abspath('../../ext_lib'),
                os.path.abspath('/usr/lib/openmpi/lib'),
                os.path.abspath(os.environ['MPI_LIB']),
                ]
            })
    elif sMode == 'mpi_nersc':
        ext_kwargs.update({
            'libraries': ['radia', 'm', 'fftw', 'mpichcxx_intel', 'dl'],
            'library_dirs': [
                os.path.abspath('../gcc'),
                os.path.abspath('../../ext_lib'),
                os.path.abspath(os.getenv('MPICH_DIR') + '/lib'),
                ]
            })
    elif sMode == '0':
        pass
    else:
        raise Exception("Unknown Radia compilation/linking option")

radia = Extension('radia', **ext_kwargs)

setup(name='radia',
      version='1.0',
      description='This is Radia for Python',
      author='O. Chubar, P. Elleaume, J. Chavanne',
      author_email='chubar@bnl.gov',
      url='http://github.com/ochubar/Radia',
      long_description='This is Python interface to the Radia 3D magnetostatic code.',
      ext_modules=[radia])
