import post.io.decompress
import numpy as np


"This script is designed to store domain information"

class read(object):
   def __init__(self,grdbasfile,wrf=False,arps=False,rst=False,**kwargs):
      #grdbasfile = Nio.open_file(path, mode = 'r', options = None, history='', format='hdf')
      if wrf:
        self.grab_attr(grdbasfile,wrf=True,**kwargs)
      elif arps:
        self.grab_attr(grdbasfile,arps=True,**kwargs)
      else:
        self.grab_attr(grdbasfile,rst=rst,**kwargs)

   def grab_attr(self,grdbasfile,wrf=False,arps=False,rst=False,**kwargs):
      idealized=True
      if wrf:
        self.ctrlat = float(grdbasfile.getncattr('CEN_LAT'))
        self.ctrlon = float(grdbasfile.getncattr('CEN_LON'))
        self.trulat1 = float(grdbasfile.getncattr('TRUELAT1'))
        self.trulat2 = float(grdbasfile.getncattr('TRUELAT2'))
        #self.trulon = float(grdbasfile.getncattr['TRUELON'])

        self.dx = float(grdbasfile.getncattr('DX'))/1000.
        self.dy = float(grdbasfile.getncattr('DY'))/1000.

        #--- Unstaggered Grid Dims
        self.nx = int(grdbasfile.getncattr('WEST-EAST_GRID_DIMENSION'))-1
        self.ny = int(grdbasfile.getncattr('SOUTH-NORTH_GRID_DIMENSION'))-1
        self.nz = int(grdbasfile.getncattr('BOTTOM-TOP_GRID_DIMENSION'))-1

        #--- Creating Grid Point Locations
        ph =  np.squeeze(grdbasfile.variables['PH'][0,:,:,:])
        phb = np.squeeze(grdbasfile.variables['PHB'][0,:,:,:])
        #--- PS height above the surface varies grid point to grid point (need full 3-D array)
        self.zf = ((ph + phb)/9.8)/1000.
        self.zh = ((self.zf[1:]+self.zf[:-1])/2.)

        #self.zh = (((ph[1:]+ph[:-1])/2.) + ((phb[1:]+phb[:-1])/2.))/9.8


        self.xh = np.zeros((self.nx))
        self.xf = np.zeros((self.nx+1))
        self.yh = np.zeros((self.ny))
        self.yf = np.zeros((self.ny+1))


        #--- Getting Regular and Staggered Coordinates
        for xindex in range(0,self.nx):
           self.xh[xindex] = (self.dx/2.) + (xindex*self.dx)
           self.xf[xindex] = xindex*self.dx
        self.xf[-1] = (self.nx)*self.dx


        for yindex in range(0,self.ny):
            self.yh[yindex] = (self.dy/2.) + (yindex*self.dy)
            self.yf[yindex] = yindex*self.dy
        self.yf[-1] = (self.ny)*self.dy

      elif arps:

         patchx = 1
         patchy = 1
         self.nx = 3+((int(grdbasfile.attributes['nx']) - 3) *patchx)
         self.ny = 3+((int(grdbasfile.attributes['ny']) - 3) *patchy)
         self.nz = int(grdbasfile.attributes['nz'])
         self.dx = float(grdbasfile.attributes['dx'])/1000.
         self.dy = float(grdbasfile.attributes['dx'])/1000.
         self.zf = run_decompress(grdbasfile,'zp')[:,0,0]/1000.#grdbasfile.variables['zp'][:,:,:] # Physical Height

         #--- Converting to Scalar Height
         z_scalar = np.zeros(self.zf.shape)
         z_tmp = (self.zf[:-1]+self.zf[1:])/2.
         z_scalar[:-1] = z_tmp
         z_scalar[-1] = np.nan
         self.zh=z_scalar

         try:
            self.zsoil = run_decompress(grdbasfile,'zpsoil',lev=0)[0,0]#grdbasfile.variables['zpsoil'][0,:,:]
         except:
            self.zsoil = np.zeros((self.ny,self.nx))[0,0]
         self.AGL_zf = self.zf - self.zsoil
         self.AGL_zh = self.zh - self.zsoil

         if idealized: #--- Follow CM1 convention (Plot by Distance)
            self.xh = np.zeros((self.nx))
            self.yh = np.zeros((self.ny))
            for xindex in range(0,self.nx):
               self.xh[xindex] = self.dx*xindex
            for yindex in range(0,self.ny):
               self.yh[yindex] = self.dy*yindex

         else: # Real Case That Requires a Map
            self.ctrlat = float(grdbasfile.attributes['ctrlat'])
            self.ctrlon = float(grdbasfile.attributes['ctrlon'])
            self.trulat1 = float(grdbasfile.attributes['trulat1'])
            self.trulat2 = float(grdbasfile.attributes['trulat2'])
            self.trulon = float(grdbasfile.attributes['trulon'])
            self.width_x = (self.nx - 1) * self.deltax
            self.width_y = (self.ny - 1) * self.deltay

      else:
        self.nx = grdbasfile.getncattr('nx')
        self.ny = grdbasfile.getncattr('ny')
        self.nz = grdbasfile.getncattr('nz')

        if rst:
           scaling = 1/1000.
        else:
           scaling = 1.

        self.xh = grdbasfile.variables['xh'][:] * scaling
        self.xf = grdbasfile.variables['xf'][:] * scaling
        self.yh = grdbasfile.variables['yh'][:] * scaling
        self.yf = grdbasfile.variables['yf'][:] * scaling
        self.zh = grdbasfile.variables['zh'][:] * scaling
        self.zf = grdbasfile.variables['zf'][:] * scaling

        self.dx = round((self.xh[1] - self.xh[0]),4)  #* 1000.


      if 'arguments' in kwargs:
         if kwargs['arguments'].xmin >= 0:
            self.xmin = kwargs['arguments'].xmin
            self.xmax = kwargs['arguments'].xmax
            self.ymin = kwargs['arguments'].ymin
            self.ymax = kwargs['arguments'].ymax
         else:
            self.xmin = 0
            self.xmax = self.nx
            self.ymin = 0
            self.ymax = self.ny

         try:
            self.lev = kwargs['arguments'].lev
         except:
            self.lev = 0
      else:
         self.xmin = 0
         self.xmax = self.nx
         self.ymin = 0
         self.ymax = self.ny
         self.lev = 0

