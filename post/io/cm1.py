import numpy as np

def readvar(dumpfile,varname,**kwargs):
   """ 
   The goal of this function is to read in CM1 variables that are requested

   *** Stagger Grids are Not Available with this Code  ***
   *** All model variables are untaggered before being ***
   *** returned.
   
   Required Arguments:
      -dumpfile:  The dumpfile used to read in CM1 output
      -varname:   The variable that is being read in


   Optional arguments:
      -Horizontal Grid Information: xmin,xmax,ymin,ymax
      -Vertical Grid Information: lev, interp_hgt
         -lev: The Model Level you plan to work with
               If lev < 0, then you take the column max value
         -interp_hgt: The vertical height you plan to work with
   """

   MAX = False #--- A boolean to determine if looking at Column Max Values

   #-------------------------#
   #  Horizontal Grid Info   #
   #-------------------------#

   if 'xmin' in kwargs:
         xmin = kwargs['xmin']
         xmax = kwargs['xmax']
         ymin = kwargs['ymin']
         ymax = kwargs['ymax']
         if xmin < 0:
            xmin = 0
            xmax = dumpfile.getncattr('nx')
            ymin = 0
            ymax = dumpfile.getncattr('ny')
         elif xmin == xmax:
            xmax = xmin+1
         elif ymin == ymax:
            ymax = ymin+1
   else:
      xmin = 0
      ymin = 0
      try:
        xmax = dumpfile.getncattr('nx')
        ymax = dumpfile.getncattr('ny')
      except:
        tmp = np.squeeze(dumpfile.variables['prs'][0,:,:,:])
        xmax = tmp.shape[-1]
        ymax = tmp.shape[-2]
        zmax = tmp.shape[-3]
   #------------------------#
   #   Vertical Grid Info   #  
   #------------------------#

   #--- Plot a Specific Model Level
   if 'lev' in kwargs:
      if kwargs['lev']<0:
         lev_a = 0
         try:
            lev_b = dumpfile.getncattr('nz')
         except:
            try:
               lev_b = dumpfile.getncattr('nk')
            except:
               lev_b = zmax
         MAX = True
      else:
          lev_a = kwargs['lev']
          lev_b = kwargs['lev']+1

   #--- Interpolate Model Output to Specific Height
   elif 'interp_hgt' in kwargs:
     if 'zh' in kwargs:
        vertical_dim = kwargs['zh']
     else:
        vertical_dim = np.squeeze(dumpfile.variables['zh'][:])
     #if vertical_dim.ndim == 3:  vertical_dim = vertical_dim[:,0,0]
     if np.amax(vertical_dim) > 1000:
        vertical_dim = vertical_dim / 1000.
     #print(kwargs['interp_hgt'])
     #min_lev = int(np.argwhere(vertical_dim < kwargs['interp_hgt'])[-1])
     #print(vertical_dim.shape)
     #min_lev = int(np.argwhere(vertical_dim < kwargs['interp_hgt']))

     try:
         min_lev = int(np.argwhere(vertical_dim < kwargs['interp_hgt'])[-1])
     except:
         min_lev = int(np.argwhere(vertical_dim[:,0,0] < kwargs['interp_hgt'])[-1])


     lev_a = min_lev
     lev_b = min_lev+2

 
   #--- Full Volume
   else:
      lev_a = 0
      try:
         lev_b = len(dumpfile.dimensions['nz'])
      except:
         try:
            lev_b = len(dumpfile.dimensions['nk'])
         except:
            lev_b = np.squeeze(dumpfile.variables['qv'][0,:,:,:]).shape[0]

   #------------------------------#
   #---- Variable Information ----#
   #------------------------------#

   try: #--- First Try to Read in Variable Directly from Model Output

      if varname in ['xh','xf','yh','yf','zh','zf','time']:
          var = np.squeeze(dumpfile.variables[varname][:])

      elif varname in ['nx','ny','nz']: #--- attribute variables
         var = dumpfile.getncattr(varname)

      elif varname in ['uh','svs','shs','sus','sus2','svs2','rain','sws','t2','q2','u10','v10']:
         var = np.squeeze(dumpfile.variables[varname][0,ymin:ymax,xmin:xmax])
  
      elif varname in ['ua','u','va','v','wa','w']:
         #--- JDL Make Sure Unstagger Process is Correct
         try:
            var_tmp = dumpfile.variables[varname][0,:,:,:]
         except:
            if varname == 'ua':
               var_tmp = dumpfile.variables['u'][0,:,:,:]
            elif varname.upper() == 'U':
               var_tmp = dumpfile.variables['ua'][0,:,:,:]
            elif varname.upper() == 'VA':
               var_tmp = dumpfile.variables['v'][0,:,:,:]
            elif varname.upper() == 'V':
               var_tmp = dumpfile.variables['va'][0,:,:,:]
            elif varname.upper() == 'WA':
               var_tmp = dumpfile.variables['w'][0,:,:,:]
            elif varname.upper() == 'W':
               var_tmp = dumpfile.variables['wa'][0,:,:,:]
        



         if varname in['ua','u']:    stag_ax = 2  #--- Staggered X-Grid
         elif varname in ['va','v']: stag_ax = 1  #--- Staggered Y-Grid
         elif varname in ['wa','w']: stag_ax = 0  #--- Staggered Z-Grid
         new_grid = unstagger_grid(var_tmp,stag_ax)
         var = np.squeeze(unstagger_grid(var_tmp,stag_ax)[lev_a:lev_b,ymin:ymax,xmin:xmax])

      else:
         var = np.squeeze(dumpfile.variables[varname][0,lev_a:lev_b,ymin:ymax,xmin:xmax])

   except: #--- If not Possible, derive the variable 

      if varname in ['rhoa','T']:
         try:
            th = np.squeeze(dumpfile.variables['th'][0,lev_a:lev_b,ymin:ymax,xmin:xmax])
         except:
            th = np.squeeze(dumpfile.variables['theta'][0,lev_a:lev_b,ymin:ymax,xmin:xmax])
         p = np.squeeze(dumpfile.variables['prs'][0,lev_a:lev_b,ymin:ymax,xmin:xmax])
         T = (th / ( (100000. / p) ** (287./1004.) )) 
         if varname == 'T':
            var = T - 273.15
         else:
            rho_air = p / (287 * T)

         #var = jl_modules.theta2temp(p,th) - 273.15

      elif varname in 'Td':
         p = np.squeeze(dumpfile.variables['prs'][0,lev_a:lev_b,ymin:ymax,xmin:xmax])
         qv = np.squeeze(dumpfile.variables['qv'][0,lev_a:lev_b,ymin:ymax,xmin:xmax])
         e=(qv/(qv+0.622))*(p/100.)
         var =  (5.42E3/((5.42E3/273.)-np.log(e/6.11))) - 273.15
         #var = jl_modules.cal_td(qv,p)

      elif varname in ['uadiff']:#--- Dirty Code Doesn't Care about staggering
         var = np.absolute(np.squeeze(dumpfile.variables['ua'][0,lev_a:lev_b,ymin:ymax,xmin:xmax]))

      elif 'pert' in varname: #varname in ['thpert','qvpert','upert','vpert','wpert']:
         #--- First Determine the Area You are averaging over
         nz_local = lev_b - lev_a
         nx_local = xmax - xmin
         ny_local = ymax - ymin

         if varname == 'thpert':
            try:
               var_tmp = np.squeeze(dumpfile.variables['th'][0,lev_a:lev_b,:,:])
            except:
               var_tmp = np.squeeze(dumpfile.variables['theta'][0,lev_a:lev_b,:,:])
         elif varname =='qvpert':
            var_tmp = np.squeeze(dumpfile.variables['qv'][0,lev_a:lev_b,:,:])
         elif varname in ['upert','vpert','wpert']:
            if varname in['upert']:    stag_ax = 2  #--- Staggered X-Grid
            elif varname in ['vpert']: stag_ax = 1  #--- Staggered Y-Grid
            elif varname in ['wpert']: stag_ax = 0  #--- Staggered Z-Grid
            try:
               var_tmp = np.squeeze(unstagger_grid(dumpfile.variables[varname[0]][0,:,:,:],stag_ax)[lev_a:lev_b,:,:])
            except:
               var_tmp = np.squeeze(unstagger_grid(dumpfile.variables[varname[0]]+'a'[0,:,:,:],stag_ax)[lev_a:lev_b,:,:])

         if nz_local == 1:
            var = var_tmp[ymin:ymax,xmin:xmax] - np.mean(var_tmp)
         else:
            if ny_local == 1:
                var = np.zeros((nz_local,nx_local))
            elif nx_local == 1:
               var = np.zeros((nz_local,ny_local))
            else:
               var = np.zeros((nz_local,ny_local,nx_local))
            for zindex,hgt in enumerate(range(lev_a,lev_b)):
               var[zindex] = var_tmp[zindex,ymin:ymax,xmin:xmax] - np.mean(var_tmp[zindex])

      elif varname in ['wspd','wdir']:
         try:
            u = np.squeeze(dumpfile.variables['uinterp'][0,lev_a:lev_b,ymin:ymax,xmin:xmax])
            v = np.squeeze(dumpfile.variables['vinterp'][0,lev_a:lev_b,ymin:ymax,xmin:xmax])
         except:
            try:
               u = np.squeeze(unstagger_grid(dumpfile.variables['ua'][0,:,:,:],2)[lev_a:lev_b,ymin:ymax,xmin:xmax])
               v = np.squeeze(unstagger_grid(dumpfile.variables['va'][0,:,:,:],1)[lev_a:lev_b,ymin:ymax,xmin:xmax])
            except:
               u = np.squeeze(unstagger_grid(dumpfile.variables['u'][0,:,:,:],2)[lev_a:lev_b,ymin:ymax,xmin:xmax])
               v = np.squeeze(unstagger_grid(dumpfile.variables['v'][0,:,:,:],1)[lev_a:lev_b,ymin:ymax,xmin:xmax])
         if varname == 'wspd':
            var = np.sqrt(u**2 + v**2)
         elif varname == 'wdir':
            var =180 + (np.arctan2(u,v) * 180./np.pi)

      elif varname == 'wmax':
         try:
            var = np.amax(np.squeeze(dumpfile.variables['winterp'][0,:,ymin:ymax,xmin:xmax]),axis=0)
         except:
            try:
               var = np.squeeze(unstagger_grid(dumpfile.variables['wa'][0,:,:,:],0)[lev_a:lev_b,ymin:ymax,xmin:xmax])
            except:
               var = np.squeeze(unstagger_grid(dumpfile.variables['w'][0,:,:,:],0)[lev_a:lev_b,ymin:ymax,xmin:xmax])
      else:
         print('The desired variable (%s) is not available'%varname)


   #--- Final Touches
   if 'interp_hgt' in kwargs:
      var = var[0] + (((var[1] - var[0])/(vertical_dim[min_lev+1] - vertical_dim[min_lev]))*(kwargs['interp_hgt']-vertical_dim[min_lev]))

   if MAX:
      var = np.amax(var,axis=0)

   if varname in ['qr','qs','qg','qh','qhl','qv','qvpert']:
      var = var * 1000.

   elif varname in ['rain']:
      var = var * 10.  # convert from cm to mm

   return var


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
