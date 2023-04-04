#!/usr/bin/env python2.7

#Code: decompress.py  (taken from decompressVariable.py)
#Version: 1.01
#Original Author: Tim Supinie
#Written: November 2014 

#Modifications:
#  Nate Snook (9 Jun. 2015) -- Edited for use with plot_var_advanced.py;
#     names of code and function changed to specify it's exclusively for use with ARPS.

import numpy as np

def run_decompress(dumpfile,var,lev=None,xmin=None,xmax=None,ymin=None,ymax=None,zmin=None,zmax=None,
                   xloc=None,yloc=None,zloc=None):
   variable = arps_decompress(dumpfile.variables[var])

   if lev is None:
      if xloc:
        #--- Get Point Location
        variable = variable[zloc,yloc,xloc]
      #--- Currently assume xmin and ymin occurr together
      #--- However Z min can be called independently
      elif zmin is None:
        if xmin is None:
          try:
            variable = variable[:,:,:]
          except:
            variable = variable[:,:]
        else:
          try:
             variable = variable[:,ymin:ymax,xmin:xmax]
          except:
             variable = variable[ymin:ymax,xmin:xmax]
      else:
        if xmin is None:
          variable = variable[zmin:zmax,:,:]
        else:
          variable = variable[zmin:zmax,ymin:ymax,xmin:xmax]
   else:
      if xmin is None:
        variable = variable[lev,:,:]
      else:
        variable = variable[lev,ymin:ymax,xmin:xmax]
   if var == 'nr':
     variable[variable<2.5] = 0.
   if var == 'nh':
     variable[variable<1E-6] = 0.0
   return variable


def arps_decompress(hd_var, dindex=None):
    """
    Decompresses variable fields from ARPS HDF files that use high compression options
    (specifically, the mapping of 32 bit --> 16 bit integers).  

    Required arguments:
        hd_var: The compressed variable field
    
    Optional arguments:
        dindex: Option to return a slice of the compressed data if only a slice is desired.
                The index may be either an integer (interpreted as an element of the first dimension) or a tuple.
                The tuple must have no more elements than the data has dimensions. Each element must be either
                an integer (a specific element along the given axis) or a Python slice object (a slice along the
                given axis). For example, dindex=(0, slice(None), slice(2, 6)) would return the first element along
                the first axis, all elements along the second axis, and elements 3-7 along the third axis (equivalent
                to asking for ary[0, :, 2:6], where ary is a numpy array).

    Returns:
        decompressed_data:  The decompressed equivalent of hd_var or the requested slice thereof.
    """
    ndim = len(hd_var.shape)
    if dindex is None:
        dindex = (slice(None),)
    elif type(dindex) == int:
        dindex = (dindex,)
    dindex = dindex + tuple([slice(None)] * (ndim - len(dindex)))

    if not hasattr(hd_var, 'min') or not hasattr(hd_var, 'max'):
        return hd_var[dindex]

    max_i16 = np.iinfo(np.int16).max
    min_i16 = np.iinfo(np.int16).min

    # Compute each grid point's fraction between the minimum and maximum
    fraction = (hd_var[dindex].astype(np.float32) - min_i16) / (max_i16 - min_i16)

    # Get the slice for the min and max arrays such that they broadcast correctly with the fraction array.
    dindex_1d = [ np.newaxis for idx in hd_var.shape ]
    if ndim <= 3:
        dindex_1d[0] = dindex[0]
    else:
        dindex_1d[-3] = dindex[-3]
    dindex_1d = tuple(dindex_1d)

    # Get another slice such that we return an array with a logical number of dimensions
    # (integer indices should remove that dimension, any slice should keep the dimension, even if it's length 1)
    dindex_nd = tuple([ 0 if type(i) == int else slice(None) for i, i1d in zip(dindex, dindex_1d) if type(i1d) != int ])

    # Get the decompressed data
    decompressed_data = hd_var.min[dindex_1d] * (1 - fraction) + hd_var.max[dindex_1d] * fraction
    return decompressed_data[dindex_nd]

if __name__ == "__main__":
    import Nio as nio
    import sys
    import traceback

    _out = sys.stdout

    file_name = "/caps2/tsupinie/ar2013052000.hdf000000"
    hdf = nio.open_file(file_name, mode='r', format='hdf')

    def test(var, dindex=None, verbose=True):
        if verbose:
            _out.write("Testing %s ... " % var)
            _out.flush()
        try:
            data = arps_decompress(hdf.variables[var], dindex=dindex)
            if verbose:
                _out.write("Success! (Min/max: %.1f/%.1f)\n" % (data.min(), data.max()))
                _out.flush()
        except Exception as e:
            if verbose:
                _out.write("Failure! (%s)\n" % str(e))
            else:
                _out.write(traceback.format_exc())

    test('tsoil', dindex=3, verbose=False)
#   test('pt', dindex=(0,0), verbose=False)
#   test('ptsflx')
#   test('x')

    hdf.close()
