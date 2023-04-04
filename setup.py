import os
import numpy as np
from setuptools import setup, find_packages, Extension

np_loc = os.path.dirname(np.__file__)

setup(
    name='post',
    version='1.0.1',
    description='Scripts used to post process model output. Includes scripts for io, plot, variable conversion, plotting',
    #packages=find_packages(),
    packages=find_packages('/work/jeremy.gibbs/post/'),
    include_package_data=True,
    author="Jeremy A. Gibbs and Jonathan Labriola",
    author_email="jeremy.gibbs@noaa.gov",
)