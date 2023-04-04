#!/usr/bin/python
from scipy import interpolate
import numpy as np
#--- Previously referred to ass jl_modules
#Code: nate_modules.py (Python Module Library)
#Author: Nate Snook (CASA/CAPS/SoM)
#Written: Dec. 2009
#Last modified:  Dec. 22, 2009
#---------------------------------------------------------------------------------#

# List of contents:

# avg( float[] )                                        --  calculates average of an array
# create_progress_bar(int, int)                         --  creates a progress bar for a loop.
# update_progress_bar(int, int)                         --  updates a progress bar created by create_progress_bar.
# vort_2d( float[:,:], float[:,:], int, int, int=1)     --  calculates vertical vorticity of 2-D array (x-y slice)
# vort_3d( float[:,:,:], float[:,:,:], int, int, int=1) --  calculates vertical vorticity of 3-D array (x,y,z)
# define_kernel(int)                                    --  calculates kernel for NEP convolution calculations

#---------------------------------------------------------------------------------#

# *** Module avg *** #
#Calculates an average using Numeric
#Required arguments -- array (a 1-D array to be averaged)
#Optional arguments -- none
#Returns -- average (float)
def avg(array):
   from Numeric import average
   the_average = average(array)
   return the_average

#---------------------------------------------------------------------------------#

# *** Module create_progress_bar *** #
#Creates a progress bar for a loop.
#Required arguments -- loopsize (the number of iterations in the loop)
#Optional arguments -- steps    (the length of the progress bar -- defaults to 20)
#                      pbtext   (label to show with the progress bar (blank by default)) 
#Returns -- pbstep (how frequently to update the progress bar)

def create_progress_bar(loopsize, steps = 20, pbtext = ''):
   from sys import stdout
   from math import ceil
   pbstep = ceil(float(loopsize) / float(steps))
   steps2 = int(ceil(float(loopsize) / float(pbstep)))
   stdout.write(pbtext + "[%s]" %(" " * (steps2 - 1)))
   stdout.flush()
   stdout.write("\b" * (steps2))
   return int(pbstep)

#---------------------------------------------------------------------------------#

# *** Module update_progress_bar *** #
#Updates a progress bar made by create_progress_bar
#Required arguments -- pbstep  (when to update the progress bar (returned by create_progress_bar))
#                      control (the loop iterator used to control the progress bar)
#Optional arguments -- <<none>>
#Returns -- <<nothing>> (updates the progress bar)

def update_progress_bar(pbstep, control):
   from sys import stdout
   if control != 0 and control%pbstep == 0:
      stdout.write("*")
      stdout.flush()

#---------------------------------------------------------------------------------#

# *** Module format_arps_time *** #
#Takes an integer number provided and converts it to the six-digit ARPS time format, which is then returned.
#Required arguments -- rawtime (The number to be converted into the ARPS time format) 
#Returns -- arpstime (rawtime converted into the ARPS time format

#IMPORTANT NOTE:  This module expects rawtime to be passed in AS A STRING.  Passing in a raw integer should 
#                 work most of the time, but leading zeroes may be an issue if rawtime is not a string!
def format_arps_time(rawtime):
   arpstime = '{:0>6}'.format(int(rawtime))
   print('Raw time ' + str(rawtime) + ' converted to ARPS time format: ' + str(arpstime))
   return arpstime

#---------------------------------------------------------------------------------#

# *** Module vort_2d *** #
#Calculates vertical vorticity on a 2-D x-y slice given a u- and v- wind field
#Required arguments -- u (u wind field as a 2-D array in the x-y plane)
#                      v (v wind field as a 2-D array in the x-y plane)
#                      dx (delta x -- x-direction grid spacing)
#                      dy (delta y -- y-direction grid spacing)
#Optional arguments -- delt (how many gridpoints radius to use in the centered difference; default 1)
#Returns -- vort (vertical vorticity as a 2-D array in the x-y plane)
def vort_2d(u, v, dx, dy, delta = 1):
   from numpy import zeros
   delt = int(delta)
   nx = len(u)
   ny = len(u[0][:])

   vort = zeros((nx,ny))
   vort[delt:-delt,delt:-delt] = (v[2*delt:, delt:-delt] - v[:-2*delt, delt:-delt])/(2 * delt * dx) - (u[delt:-delt, 2*delt:] - u[delt:-delt, :-2*delt])/(2 * delt * dy)

   return vort

#---------------------------------------------------------------------------------#

# *** Module vort_3d *** #
#Calculates vertical vorticity for a 3-D domain given a u- and v- wind field
#Required arguments -- u (u wind field as a 3-D array (x,y,z))
#                      v (v wind field as a 3-D array (x,y,z))
#                      dx (delta x -- x-direction grid spacing)
#                      dy (delta y -- y-direction grid spacing)
#Optional arguments -- delt (how many gridpoints radius to use in the centered difference; default 1)
#Returns -- vort (vertical vorticity as a 2-D array in the x-y plane)
def vort_3d(u, v, dx, dy, delta = 1):
   from numpy import zeros
   delt = int(delta)
   nz = len(u[0][0][:])
   ny = len(u[0][:])
   nx = len(u)

   vort = zeros((nx,ny,nz))
   vort[delt:-delt,delt:-delt,:] = (v[(2*delt):,delt:-delt,:]-v[:-(2*delt),delt:-delt,:])/((2*delt)*dx) - (u[delt:-delt,(2*delt):,:]-u[delt:-delt,:-(2*delt),:])/((2*delt)*dy)

   return vort


#---------------------------------------------------------------------------------#

# *** Module air_density *** #
#Calculates air density for a 3-D domain given pressure and potential temperature
#Returns -- rho_air (air density as a 3-D array)

def air_density(p, pt):
   from numpy import shape, zeros 
   R = 287.            # J[kg * K]^-1
   cp = 1004.          # J[kg * K]^-1
   R_over_cp = R / cp  # J[kg * K]^-1
   p_0 = 100000.        # base state pressure of 1000 mb = 100000 Pa  

   #air density
   rho_air = zeros(shape(p))

   #temperature (in kelvin) from potential temperature equation
   T = pt / ( (p_0 / p) ** R_over_cp ) 

   #Calculate air density using ideal gas law
   rho_air = p / (R * T)

   #print 'Air density:  maximum = ' + str(rho_air.max()) + '  |  minimum = ' + str(rho_air.min())

   return rho_air

#---------------------------------------------------------------------------------#


# *** temperature

def theta2temp(p,pt):
  R = 287.            # J[kg * K]^-1
  cp = 1004.          # J[kg * K]^-1
  R_over_cp = R / cp  # J[kg * K]^-1
  p_0 = 100000.
  T = pt / ( (p_0 / p) ** R_over_cp )
  return T

#----------------------------------------------------------------------------------------#

def temp2theta(p,T):
  """
  Calculate potential temperature from temperature

  p (pa)
  T (k)
  """
  R = 287.            # J[kg * K]^-1
  cp = 1004.          # J[kg * K]^-1
  R_over_cp = R / cp  # J[kg * K]^-1
  p_0 = 100000.
  pt = T *  ( (p_0 / p) ** R_over_cp )
  return pt


#----------------------------------------------------------------------------------------#

def cal_rh(p,th,qv):
  """
  Calculate the relative humidity
  """

  T = theta2temp(p,th)
  es = cal_es(T)
  e = cal_e(qv,p)

  return ((100.*e)/es)

#----------------------------------------------------------------------------------------#


def setup_subdomain(xmin, xmax, ymin, ymax, dx, dy, trulat1, trulat2, var2d, fullmap):
   from mpl_toolkits.basemap import Basemap
   from numpy import meshgrid, arange
   #Define center lat, lon of the subdomain:
   xctr = int(((xmax + xmin) / 2)*dx)
   yctr = int(((ymax + ymin) / 2)*dy)

   lonctr, latctr = fullmap(xctr, yctr, inverse = True)

   #Trim arrays (including overlays, if applicable)
   var2d = var2d[ymin:ymax, xmin:xmax]
#   if arguments.overlay_vort:
#       vort_sfc = vort_sfc[ymin:ymax, xmin:xmax]
#   if arguments.show_windvect or arguments.show_windbarbs:
#       u_sfc_kts = u_sfc_kts[ymin:ymax, xmin_xmax]
#       v_sfc_kts = v_sfc_kts[ymin:ymax, xmin_xmax]
#   #end if

   width_x = float(xmax - xmin - 1)*dx
   width_y = float(ymax - ymin - 1)*dy

   x = arange(0, width_x+dx, dx)
   y = arange(0, width_y+dy, dy)

   x, y = meshgrid(x,y)

   print("-----     -----     -----")
   print('Plot will show the following subdomain:')
   print('x:  (' + str(xmin) + ',' + str(xmax) + ')')
   print('y:  (' + str(ymin) + ',' + str(ymax) + ')')
   print('New ctrlat, ctrlon: (' + str(latctr) + ',' + str(lonctr) + ')')
   print('New map will use lat_1 of ' + str(trulat1) + ' and lat_2 of ' + str(trulat2) + '.')
   print("-----     -----     -----")

   map = Basemap(projection='lcc', width=width_x, height=width_y, lat_1=trulat1, lat_2=trulat2, lat_0=latctr, lon_0=lonctr, resolution='h', area_thresh=10.)  #New lambert conformal map for subdomain.

   return(map, x, y, var2d)
#end def(setup_subdomain)

#-------------------------------------------------------------------------------#

def define_kernel(radius, dropoff=0.0):
   from sys import exit
   #from numpy import zeros, array, shape, floor
   import numpy as np

   #Valid keyword arguments: 
   #  dropoff  --  value between 0 and 1 to reduce influence of points near edge of neighborhood
   #               (values closer to 1 will result in greater dropoff with range).

   #print 'Radius of ' + str(radius) + ' given.'

   #Check for valid positive radius
   if radius < 0:
      exit('ERROR: Invalid neighborhood radius -- radius cannot be negative!')

   kernel = np.zeros((int((2*np.floor(radius))+1), int(2*(np.floor(radius))+1    )))
   for i in range(0,kernel.shape[0]):
      for j in range(0,kernel.shape[1]):
         icoord = abs(i - (np.floor(radius)))
         jcoord = abs(j - (np.floor(radius)))
         if ((icoord*icoord) + (jcoord*jcoord) <= (radius*radius)):
            kernel[i, j] = 1.0 - ( ((icoord*icoord) + (jcoord*jcoord)) / (radius*radius) ) * dropoff
         #end if
      #end for
   #end for

   #Return the valid kernel array 
   return(kernel)

#end def(define_kernel)

#-----------------------------------------------------------------------------------#

def define_kernel_ellipse(xradius, yradius, dropoff=0.0):
   from sys import exit
   from numpy import zeros, array, shape, floor

   #Valid keyword arguments: 
   #  dropoff  --  value between 0 and 1 to reduce influence of points near edge of neighborhood
   #               (values closer to 1 will result in greater dropoff with range).

   print('Elliptical neighborhood selected.')
   print('north/south radius:' + str(xradius) + ' gridpoints  |  east/west radius: ' + str(yradius) + ' gridpoints')

   #Check for valid positive radius
   if xradius < 0 or yradius < 0:
      exit('ERROR: Invalid ellipse settings -- semi-minor/semi-major axes cannot be negative!')

   kernel = zeros(((2*floor(yradius))+1, 2*(floor(xradius))+1    ))
   for i in range(0,kernel.shape[0]):
      for j in range(0,kernel.shape[1]):
         icoord = abs(i - (floor(yradius)))
         jcoord = abs(j - (floor(xradius)))
         if ( ((icoord*icoord) / (yradius*yradius)) + ((jcoord*jcoord) / (xradius*xradius)) <= 1.0 ):
            kernel[i, j] = 1.0 - ( ((icoord*icoord)/(yradius*yradius)) + ((jcoord*jcoord)/(xradius*xradius)) ) * dropoff
         #end if
      #end for
   #end for

   #Return the valid kernel array 
   return(kernel)

#end def(define_kernel)

#------------------------------------------------------------------#
#  Since the CAPS installation of Python2.7 does not include the
#  Matplotlib function matplotlib.colors.from_levels_and_colors,
#  I have reproduced its functionality here from the github code
#  (https://github.com/matplotlib/matplotlib/pull/2050)

def from_levels_and_colors(levels, colors, extend='neither'):
   """
   A helper routine to generate a cmap and a norm instance which
   behave similar to contourf's levels and colors arguments.

   Parameters
   ----------
   levels : sequence of numbers
       The quantization levels used to construct the :class:`BoundaryNorm`.
       Values ``v`` are quantizized to level ``i`` if
       ``lev[i] <= v < lev[i+1]``.
   colors : sequence of colors
       The fill color to use for each level. If `extend` is "neither" there
       must be ``n_level - 1`` colors. For an `extend` of "min" or "max" add
       one extra color, and for an `extend` of "both" add two colors.
   extend : {'neither', 'min', 'max', 'both'}, optional
       The behaviour when a value falls out of range of the given levels.
       See :func:`~matplotlib.pyplot.contourf` for details.

   Returns
   -------
   (cmap, norm) : tuple containing a :class:`Colormap` and a \
                  :class:`Normalize` instance
   """

   import matplotlib.colors

   colors_i0 = 0
   colors_i1 = None

   if extend == 'both':
       colors_i0 = 1
       colors_i1 = -1
       extra_colors = 2
   elif extend == 'min':
       colors_i0 = 1
       extra_colors = 1
   elif extend == 'max':
       colors_i1 = -1
       extra_colors = 1
   elif extend == 'neither':
       extra_colors = 0
   else:
       raise ValueError('Unexpected value for extend: {0!r}'.format(extend))

   n_data_colors = len(levels) - 1
   n_expected_colors = n_data_colors + extra_colors
   if len(colors) != n_expected_colors:
       raise ValueError('With extend == {0!r} and n_levels == {1!r} expected'
                        ' n_colors == {2!r}. Got {3!r}.'
                        ''.format(extend, len(levels), n_expected_colors,
                                  len(colors)))

   cmap = matplotlib.colors.ListedColormap(colors[colors_i0:colors_i1], N=n_data_colors)

   if extend in ['min', 'both']:
       cmap.set_under(colors[0])
   else:
       cmap.set_under('none')

   if extend in ['max', 'both']:
       cmap.set_over(colors[-1])
   else:
       cmap.set_over('none')

   cmap.colorbar_extend = extend

   norm = matplotlib.colors.BoundaryNorm(levels, ncolors=n_data_colors)
   return cmap, norm
#end def(from_levels_and_colors)

#------------------------------------------------------------------#
#  A function to define default thresholds and colorbar for plotting
#  various fields.
#
#  For unknown fields, passing in a max and min value will generate 
#  a generic 20-gradation colorbar.  If max and min data are missing,
#  -100 to 100 will be assumed as a last resort.

def thresh_setup(var, max = 100.0, min = -100.0, tornado=False):
   from numpy import arange
   from math import ceil

   no_proportional = False  #By default, use a proportional colorbar.

   if var == 'temp2m':
      thresholds = arange(30., 93., 3.)
      cb_ticks = [30, 40, 50, 60, 70, 80, 90]
      colormap = coldhot_20
   elif var in ['dewpk2', 'dewp2m']:
      thresholds = arange(10., 73., 3.)
      cb_ticks = [10, 20, 30, 40, 50, 60, 70]
      colormap = drywet_20
   elif var == 'sfpres':
      if tornado == False:
         thresholds = arange(920., 1004., 4.)
         cb_ticks = [920, 940, 960, 980, 1000]
         colormap = rainbow_20
      else:
         thresholds = arange(840., 1008., 8.)
         cb_ticks = [840, 880, 920, 960, 1000]
         colormap = rainbow_20
   elif var in ['pt', 'theta']:
      thresholds = arange(280., 322., 2.)
      cb_ticks = [280, 285, 290, 295, 300, 305, 310, 315, 320]
      colormap = coldhot_20
   elif var in ['temp','Temp','Temperature','temperature']:
      #thresholds = np.arange(27,32,0.25)
      #cb_ticks  = np.arange(27,32, 1.)
      #colormap = coldhot_20
      thresholds = np.arange(24.5,34.5,0.5)
      cb_ticks = np.arange(24.5,34.5,1)
      colormap = coldhot_20
   elif var in ['Z', 'truref', 'Zdm', 'refl2d', 'refl3d', 'refl','obsordr_zhh','zh','zr','zg','zs']:
      thresholds = arange(5., 85., 5.)
      cb_ticks = [10., 20., 30., 40., 50., 60., 70.]
      colormap = refl_colors_adv
   elif var in ['zdr', 'Zdr', 'zdr_3d', 'zdr_2d','obsordr_zdr']:
      thresholds =  [-3.0, -2.0, -1.5, -1.0, -0.5, -0.01, 0.01, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.50, 4.00, 4.50, 5.00]
      cb_ticks = [-3.0, -2.0, -1.0, 0, 1.0, 2.0, 3.0, 4.0, 5.0]
      colormap = altzdr
   elif var in ['dmaxg']:
      thresholds = [0.0,2.0,3.0,4.0, 5.0, 6.0, 7.0,8.0,9.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0]
      cb_ticks = [0.0,5.0,10.0,15.0,20.0,25.0,30.0]
      colormap = hail_maxdiam
   elif var in ['rhohv', 'rho_hv', 'rhv', 'rhv_2d', 'rhv_3d','obsordr_rhv']:
      thresholds = [-0.01, 0.00, 0.20, 0.40, 0.55, 0.65, 0.75, 0.80, 0.85, 0.90, 0.925, 0.95, 0.96, 0.97, 0.98, 0.99, 1.00, 1.05]
      cb_ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 0.9, 0.95, 1.00]
      colormap = rho_hv
      no_proportional = True
   elif var in ['vr', 'radv2d', 'radv3d', 'radv', 'radvel','obsordr_vr']:
      thresholds = [-30., -25., -20., -15., -10., -8., -6., -4., -2., -1., 0., 1., 2., 4., 6., 8., 10., 15., 20., 25., 30.]
      cb_ticks = [-30, -20, -10, -5, 0, 5, 10, 20, 30]
      colormap = vr_20
   elif var == 'alpha' or var == 'Alpha' or var == 'alph_h' or var == 'alph_r' or var == 'alph_g':
      #contours = [0.0,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0]
      #thresholds = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
      thresholds = np.arange(0,0.15,0.01)
      #thresholds = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.5,2.0,2.5,3.0,4.0]
      colormap = bluered_gradient
      cb_ticks = thresholds[::2]
      #cb_ticks = [0.0,0.25,0.5,0.75,1.0,1.5,2.0,3.0,4.0]#[2.0,4.0,6.0,8.0,10.0,12.0]
   elif var == 'zp':
      thresholds = [-10, 0, 50, 100, 150, 200, 300, 500, 750, 1000, 1300, 1700, 2200, 2800, 3200, 3500, 4000]
      cb_ticks = [0, 500, 1000, 2000, 3000, 4000]
      colormap = terrain_colors
   elif var == 'qv':
      #thresholds = [0,0.00025,0.0005,0.00075,0.001,0.0015,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.010,0.012,0.014,0.016]
      #cb_ticks = arange(0,0.017,0.002)
      #thresholds = [0,0.0000025,0.00005,0.000075,0.0001,0.0015,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.010,0.012,0.014,0.016]
      thresholds = [0,0.0000025,0.00005,0.000075,0.001,0.002,0.004,0.006,0.008,0.010,0.012,0.014,0.016,0.018,0.020,0.022]

      cb_ticks = thresholds#arange(0,0.017,0.002)
      colormap = greenwhitebrown
      #thresholds = arange(0.00, 0.022, 0.002)
      #cb_ticks = [0.00, 0.004, 0.008, 0.0012, 0.016, 0.020]
      #colormap = teal_gradient_20
   elif var == 'qr':
      #thresholds = arange(0.00, 0.0105, 0.0005)
      thresholds = arange(0.0000,0.0000105,0.0000005)
      #cb_ticks = [0.00, 0.002, 0.004, 0.006, 0.008, 0.010]
      cb_ticks = thresholds
      colormap = precip_20
   elif var in ['qh', 'qg', 'qs']:
      thresholds = [0.00, 0.00025, 0.00050, 0.00075, 0.0010, 0.0015, 0.002, 0.0025, 0.003, 0.0035, 0.004, 0.0045, 0.005, 0.0055, 0.006, 0.0065, 0.007, 0.0075, 0.008, 0.009, 0.010]
      #thresholds = [0.00,1E-6,1E-5,1E-4,1E-3,1E-2,1E-1,1E0]
      cb_ticks = [0.00, 0.002, 0.004, 0.006, 0.008, 0.010]
      colormap = iceprecip_20
   elif var in ['mh', 'mg', 'ms','qx_sfc']:
      thresholds = [0.00,1E-5,1E-3,0.01, 0.05, 0.10, 0.2, 0.4, 0.6, 0.8, 1.0, 1.25, 1.50, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0]
      #thresholds = [0.00, 0.0001, 0.01, 0.10, 0.2, 0.4, 0.6, 0.8, 1.0, 1.25, 1.50, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0, 4.5, 5.0]

  
      melt_contours = [0.00,1E-5,1E-4,1E-3,1E-2,1E-1,0.2,0.3,0.6,0.8,1.0,1.25,1.50,1.75,2.0,2.25,2.5,2.75,3.0]
      thresholds = melt_contours
      cb_ticks = melt_contours[::2]
      #cb_ticks = [0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0]
      colormap = iceprecip_20
   elif var == 'mr':
      #thresholds = [0.00, 0.01, 0.05, 0.10, 0.2, 0.4, 0.6, 0.8, 1.0, 1.25, 1.50, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0, 4.5, 5.0]
      thresholds = [0.00,1E-3,0.01, 0.05, 0.10, 0.2, 0.4, 0.6, 0.8, 1.0, 1.25, 1.50, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0]
      cb_ticks = [0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0]
      colormap = precip_20
   elif var == 'rhoh':
      thresholds = np.arange(880,940,5)
      cb_ticks = np.arange(880,940,10)
      colormap = pcy_20

   elif var in ['wspd', 'windspeed']:
      if tornado == True:
         thresholds = [0.0, 20.0, 29.0, 38.0, 50.0, 61.0, 74.0, 90.0, 100.0]
         cb_ticks = [0.0, 29.0, 38.0, 50.0, 61.0, 74.0, 90.0]
         colormap = efscale
      else:
         thresholds = [0.00, 0.50, 1.0, 2.0, 3.0, 4.0, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0, 27.5, 30.0]
         cb_ticks = [0.0, 2.5, 5.0, 7.5, 10.0, 20.0, 30.0]
         colormap = bluered_gradient
   elif var in ['vort', 'zvort', 'xvort', 'yvort']:
      if tornado == True:
         thresholds = arange(0.00, 2.10, 0.10)
         cb_ticks = [0.0, 0.5, 1.0, 1.5, 2.0]
         colormap = rainbow_grad_20
      else:
         thresholds = arange(0.00, 0.21, 0.01)
         cb_ticks = [0.0, 0.05, 0.1, 0.15, 0.2]
         colormap = rainbow_grad_20
   elif var in ['nh','ng','nr','ns','ntxsfc']:
      #thresholds = arange(0,2,.1)
      #thresholds  = arange(0,300,15)
      thresholds = [1e-4,1e-3,1e-2,1e-1,1,5,10,25,50,75,100,200,300]
      cb_ticks = [1e-4,1e-3,1e-2,1e-1,1,5,10,50,100,300]
      #thresholds = #[0,0.1,0.25,0.5,0.75,1.0,2.5,5,7.5,10,25,50,75,100,250,500,750,1000]#[0,0.1,0.5,1.0,5,10,50,100,500,1000]
      #cb_ticks = arange(0,300,30)#[1,10,100,1000]#arange(0,2,0.2)
      colormap = pcy_20
   elif var in ['ng']:
      thresholds  = arange(0,20000,1000)
      cb_ticks = arange(0,20000,2000)
      colormap = pcy_20
   elif var in ['w','W']:
      #thresholds = arange(1,10,0.5)
      #cb_ticks = arange(1,10,1)
      thresholds = arange(1.0,2.0,0.05)
      cb_ticks = arange(1,2,.1)
      colormap = hail_maxdiam
   elif var in ['wind']:
      thresholds = arange(10,30,1)
      cb_ticks = arange(10,30,2)
      colormap = hail_maxdiam    
   elif var in ['mmdi_r']:
      thresholds = arange(0,5,.25)
      cb_ticks = arange(0,5,1)
      colormap = pcy_20  
   elif var in ['mmdi_h','mmdi_g','mmdi_s','mmdi_r','dmxsfc']:
      #thresholds = arange(0,10,0.5)
      #cb_ticks = arange(0,10,1)
      #colormap = pcy_20
      thresholds = [0.0, 1.0,  2.0,  3.0,  4.0,  5.0,  6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0,24.0,26.0,28.0,30.0]
      cb_ticks = [0.0,5.0,10.0,15.0,20.0,25.0,30.0]
      colormap = hail_maxdiam
   elif var in ['mmdi_gh']:
      thresholds = arange(0,1,0.05)
      cb_ticks = arange(0,1,.1)
      colormap = pcy_20
   elif var == 'p':
      thresholds = arange(93000,97000,250)
      cb_ticks= arange(93000,97000,500)
      colormap =  yelloworangeblue
   else:
      thresholds = arange(min, max + ((max - min) / 20.), ((max - min) / 20.))
      cb_ticks = arange(min, max + ((max - min) / 20.), ((max - min) / 5.))
      colormap = centered_grad_20
   #end if/elif/else block

   return(thresholds, cb_ticks, colormap, no_proportional)
#end def (thresh_setup)

#--------------------------------------------------------------------------------#
#  Convert from Grid Height to scalar height (all values but w use this)
def zp_to_scalar(zp):
    import numpy
    zp_scalar = numpy.zeros(zp.shape)
    zp = (zp[:-1]+zp[1:])/2.
    zp_scalar[:-1] = zp
    return zp_scalar   
 
#--------------------------------------------------------------------------------#
# Calculate the Water Fraction Based Upon Jung et al. (2008)
# Returns the melting ice mixing ratio and number concentration

def waterFraction(qr,qi,ni,fo,rhoi,rhoa):
  import numpy as np

  mixed_frac = np.where((qr >0) & (qi > 0), fo*(np.minimum(qi/qr,qr/qi))**0.3,0.)
  fracqr = mixed_frac * qr
  fracqi = mixed_frac * qi
  fm = fracqr+fracqi
  fw = np.where(fm>0,fracqr/fm,0)

  rhom = (1000.*(fw**2)) + (1-(fw**2))*rhoi

  cx = (np.pi/6.)*rhoi
  cxm = (np.pi/6.)*rhom

  #if ni >  1e-8 :
  mmdi = np.where(ni>1e-8,((rhoa*qi)/(cx*ni))**(1./3.),0.0)
  ntm =np.where(ni>1e-8, (rhoa*fm)/(cxm * mmdi**3.),0.)
  #mmdi[ni<1e-8] = 0.0
  #ntm[ni<1e-8] =0.0 
  #else:
  #  ntm = 0.
  #  fm = 0.

  return ntm,fm,rhom

#--------------------------------------------------------------------------------#
# Calculate Lamda given alpha, cx, ntx, rhoa
def cal_Lamda(alpha,cx,ntx,qx,rhoa,mu):
  import scipy.special

  gammaOne = scipy.special.gamma(float(1.+alpha)/float(3.0*mu))
  gammaFour = scipy.special.gamma(float(4.+alpha)/float(3.0*mu))

  lamda = ((gammaFour/gammaOne)*cx*ntx/(rhoa*qx))**float(mu)

  lamda[qx<1e-8] = 0.0

  return lamda
#--------------------------------------------------------------------------------#

def cal_td(qv,p):
   """
   Calculating dewpoint temperature
   inputs: water vapor (kg/kg)
           air pressure (pa)  

   returns: dewpoint temp (C) 
 
   """
   e=(qv/(qv+0.622))*(p/100.)
   return (5.42E3/((5.42E3/273.)-np.log(e/6.11))) - 273.15

  
#--------------------------------------------------------------------------------#

def cal_es(T):
   """
   Using the Classius-Claperyon Equation to Calculate Saturation Vapor Pressure

   Input:
   T:   Air Temperature [K]
  
   Returns:
   es:  Saturated vapor pressure [Pa]
   """
   if np.amax(T) < 100:
      print('Warning Converting T to K from C')
      T += 273.15 

   es = 6.11 * np.exp(5.42E3 *((1./273.) - (1./T))) # Units are hPa

   return es * 100.

#--------------------------------------------------------------------------------#

def cal_e(qv,p):
   """
   Calculate water vapor pressure

   Input:
   p :   Air pressire [Pa]
   qv:   Water vapor mixing ratio [g/kg]
  
   Returns:
   es:  Vapor pressure [Pa]
   """
   
   if np.amax(qv > 1):
      print('Warning converting qv from g/kg to kg/kg')
      qv = qv/1000.
   return  p *qv / (0.622 + qv)

def e_to_qv(e,p):
  """
  Get qv given vapor pressure and atmopsheric pressure
  """

  return (0.6222*e)/(p-e)



#--------------------------------------------------------------------------------#
# Calculate Lamda given alpha, cx, ntx, rhoa
#def cal_Lamda(alpha,cx,ntx,qx,rhoa,mu):
#  import scipy.special
#
#  gammaOne = scipy.special.gamma((1.+alpha)/(3.0*mu))
#  gammaFour = scipy.special.gamma((4.+alpha)/(3.0*mu))
#
#  lamda = ((gammaFour/gammaOne)*cx*ntx/(rhoa*qx))**(1./3.)
#
#  return lamda
#--------------------------------------------------------------------------------#


# Calculate N0 given alpha, lamda, ntx
#def cal_N0(alpha,lamda,ntx):
#
#  import scipy.special 
#
#  gammaOne = scipy.special.gamma((1.+alpha)/(3.0*mu))
#  gammaFour = scipy.special.gamma((4.+alpha)/(3.0*mu))
#
#  n0x = ntx * (lamda**(1.+alpha)) / gammaOne

#  return n0x
#--------------------------------------------------------------------------------#

# Calculate N0 given alpha, lamda, ntx
def cal_N0(alpha,lamda,ntx,mu):

  import scipy.special

  gammaOne = scipy.special.gamma(float(1.+alpha)/float(3.0*mu))
  gammaFour = scipy.special.gamma(float(4.+alpha)/float(3.0*mu))

  n0x = 3.0*mu*ntx * (lamda**(float(1.+alpha)/float(3.0*mu))) / gammaOne

  return n0x
#--------------------------------------------------------------------------------#

# Calculate Number Concentration
def cal_Nt(N0x,qx,alpha,cx,rhoa):
  import scipy.special
  gammaOne = scipy.special.gamma(1.+alpha)
  gammaFour = scipy.special.gamma(4.+alpha)

  Ntx = ((N0x*gammaOne)**(3./(4.+alpha)))*((gammaOne/gammaFour)*rhoa*(qx/cx))**((1.+alpha)/(4.+alpha))

  return Ntx

#--------------------------------------------------------------------------------#

def smoothObs(obs,**kwargs):
   """
   Return a cleaned up radar observation
   Runs a 9 Point Smoother
   ** Dont use unless for plotting

   obs should have dimensions of [nz,ny,nx]

   Required arguments:
      obs:  Observations


   Returns:
      smooth_obs
   """
   from scipy import signal as sg
   from scipy import signal as sg
   if 'kernel_radius' in kwargs:
     kernel_radius = kwargs['kernel_radius']
   else:
     kernel_radius = 1.5
   kernel = define_kernel(kernel_radius)
   smooth_obs = sg.convolve2d(obs, kernel, mode='same', boundary='fill', fillvalue=0)
   smooth_obs = smooth_obs / kernel.sum()

   return smooth_obs

#------------------------------------------------------------------------#


def cal_dmax(alpha,lamda,n0):

   """
    Calculate maxmimum size of a hydrometeor

    alpha,lamda,n0 are three dimensional arrays

    Required arguments:
        alpha: shape parameter
        lamda: slope parameter
        n0: intercept parameter

    Returns:
       The maximum hail size
   """
 
   if type(alpha) is float:
     [ny,nx] = lamda.shape
     diameter = np.arange(0,.15,.001)
     diameter = np.tile(diameter,(nx,ny,1))
     diameter = diameter.T
 
     N_D = n0*(diameter**(alpha))*np.exp(-lamda*diameter[:])
     N_D[N_D<1e-4] = 9999
     D_max = np.where((N_D == np.amin(N_D,axis=0))&(np.amin(N_D,axis=0)!=9999),diameter,0)
   else:
     [ny,nx] = alpha.shape

     diameter = np.arange(0,.15,.001)
     diameter = np.tile(diameter,(nx,ny,1))
     diameter = diameter.T

     N_D = n0*(diameter**(alpha))*np.exp(-lamda*diameter[:])
     N_D[N_D<1e-4] = 9999
     D_max = np.where((N_D == np.amin(N_D,axis=0))&(np.amin(N_D,axis=0)!=9999),diameter,0)

   return np.amax(D_max,axis=0) * 1000.


#------------------------------------------------------------------------#

def find_coordinates(grdbas,xmin,xmax,ymin,ymax):
   """   
   Get the coordinates of a shrunken domain
   Required arguments:
   xmin (km)
   xmax (km) 
   ymin (km)
   ymax (km)
   """
   xmin_gp = int((xmin - grdbas.xh[0])/(grdbas.dx))
   xmax_gp = int((xmax - grdbas.xh[0])/(grdbas.dx))
   ymin_gp = int((ymin - grdbas.yh[0])/(grdbas.dx))
   ymax_gp = int((ymax - grdbas.yh[0])/(grdbas.dx))

   if xmin_gp < 0:
      xmin_gp = 0
   if ymin_gp < 0:
      ymin_gp = 0
   if xmax_gp > grdbas.nx:
      xmax_gp = grdbas.nx
   if ymax_gp > grdbas.ny:
      ymax_gp = grdbas.ny

   return xmin_gp,xmax_gp,ymin_gp,ymax_gp

#------------------------------------------------------------------------#

def find_coordinate(grdbas,xpt,ypt):
   """
   Get the coordinates of single grid point
   Required arguments:
   xpt (km)
   ypt (km)
   """

   xpt_gp = int((xpt - grdbas.xh[0])/(grdbas.dx))
   ypt_gp = int((ypt - grdbas.yh[0])/(grdbas.dx))

   if xpt_gp < 0:
      xpt_gp = 0
   elif xpt_gp > grdbas.nx:
      xpt_gp = grdbas.nx
   if ypt_gp < 0:
      ypt_gp = 0
   elif ypt_gp > grdbas.ny:
      ypt_gp = grdbas.ny

   return xpt_gp,ypt_gp

def unstagger_grid(var,axis):
   """
   Program to unstagger grids
   Required Inputs:
   var:  array with an undetermined number of dimensions
   axis: The axis to perform "unstaggering"

   """

   if axis == 0:
      var = (var[1:] + var[:-1]) / 2.
   elif axis == 1: 
      var = (var[:,1:] + var[:,:-1]) / 2.
   elif axis == 2: 
      var = (var[:,:,1:] + var[:,:,:-1]) / 2.
   elif axis == 3: #--- Unlikely to ever happen
      var = (var[:,:,:,1:] + var[:,:,:,:-1]) / 2.
   return var

def vertical_interp(var,z,interp_hgt):
   """
   Program that interpolates an array to a specific layer height
   var:  The Variable array to be interpolated : [nz, ny, nx]
   z:  The array of model height coordinates [nz]
   interp_hgt:  The height we are interpolating too: int
   """

   min_lev = int(np.argwhere(z < interp_hgt)[-1])
   var_low = var[min_lev]   
   var_hi = var[min_lev+1]
   var = var_low + (((var_hi - var_low)/(z[min_lev+1] - z[min_lev]))*(interp_hgt-z[min_lev]))
   return var

