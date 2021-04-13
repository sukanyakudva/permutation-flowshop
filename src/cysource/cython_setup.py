"""
permutation-flowshop repository

Build C binary code using Cython library
"""
from setuptools import setup
from Cython.Build import cythonize
setup(
    ext_modules=cythonize('calculations.pyx'),
    zip_safe=False,
)
