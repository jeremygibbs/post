import argparse
import os
import numpy as np
from netCDF4 import Dataset
import post.io



path = '/work/jonathan.labriola/TurbPBLExp/restart_files_turbulent_PBL/all/LES_02/cm1rst_000006.nc'
dumpfile = Dataset(path,"r",fortmat="NETCDF4")
va = post.io.cm1.readvar(dumpfile,'ua',lev=2)
print(va.shape)
