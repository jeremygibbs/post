import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import post.plot.colormaps
from matplotlib.patches import Polygon
def plotVar(model_output,varname,pcolor = True,HOV = False,polygon=True,**kwargs):
   """
   Goal: Plot horizontal cross sections of model variables on the figure

   #--- Overall Figure
   grdbas:          object
   figure:          object  #--- Currently made in the program, not passed in

   #--- Original Figure
   var:             string
   outpath:         string
   model_output:    [ny,nx] matrix

   #--- Contouring
   contour_output:  [ny,nx] matrix
   contour_var:     string
   contours   :     array of contouring values
   ####colormap   :     array of hexcolors
   ####mask_hgt   :     [ny,nx] matrix of surface heights


   #--- Plotting Point Plots (Currently Incapable)
   xpt              array[npts]: Of grid point locations
   ypt              array[npts]: Of grid point locations
   xpt_dis          array[npts]: Of Distanct locations (km)
   ypt_dis          array[npts]: Of Distance Locations (km)
 
   Required arguments:
      var: The Variable name (String)
      model_output: The model variable being contoured
   """

   #--- Making Figure (either pcolor or contourf)
   contours,cb_ticks,colormap = post.plot.colormaps.define_contours(varname)
   pcolor = 'True'
   figure = plt.figure()
   ax = figure.add_subplot(111)
   #--- Using Grdbas Information To Extract Plot Grid
   if 'grdbas' in kwargs:
      grdbas = kwargs['grdbas']
      plt.ylabel('Distance (km)')
      if HOV: # --- Hovmoeller Diagram
         xx,yy = np.meshgrid(grdbas.th[:],grdbas.yh[:])
         plt.xlabel('Time (s)')

      else:
         if grdbas.xmax - grdbas.xmin <= 1: #--- Vertical Cross-Section in Y-Direction
            xx,yy = np.meshgrid(grdbas.yh[grdbas.ymin:grdbas.ymax],grdbas.zh[:])
            plt.xlabel('Distance (km)')
            plt.ylabel('Height (km)')
            plt.ylim([0,6.0]) #2.5])
         elif grdbas.ymax - grdbas.ymin <= 1:  #--- Vertical Cross-Section in X-Direction
            if grdbas.zh.ndim == 1:
               xx,yy = np.meshgrid(grdbas.xh[grdbas.xmin:grdbas.xmax],grdbas.zh[:])
            else:
               xx,yy = np.meshgrid(grdbas.xh[grdbas.xmin:grdbas.xmax],grdbas.zh[:,0,0])#grdbas.xmin:grdbas.xmax,grdbas.ymin:grdbas.ymax])
            plt.ylim([0,1.5])#2.5])
            plt.xlabel('Distance (km)')
            plt.ylabel('Height (km)')
            print('HEY B')
         else: #--- Planar View
            xx,yy = np.meshgrid(grdbas.xh[grdbas.xmin:grdbas.xmax],grdbas.yh[grdbas.ymin:grdbas.ymax])
            plt.xlabel('Distance (km)')
            plt.ylabel('Distance (km)')

      if 'xpt' in kwargs:
         kwargs['xpt'] = grdbas.xh[kwargs['xpt']+grdbas.xmin]
 
      if 'ypt' in kwargs:
         kwargs['ypt'] = grdbas.yh[kwargs['ypt']+grdbas.ymin]

   else: #--- No Grid Information Available, Just Plot Number of Grid Points
      [ny,nx] = model_output.shape
      xx,yy = np.meshgrid(np.arange(0,nx),np.arange(0,ny))


   #--- Adding Color Contours to the Figure
   #--- Either Using Pcolor or Contourf
   if pcolor:
      try:
         cmap = matplotlib.colors.ListedColormap(colormap,cb_ticks)
         norm = matplotlib.colors.BoundaryNorm(contours,ncolors=len(colormap),clip=True)
         CS = plt.pcolormesh(xx,yy,model_output,cmap=cmap,norm=norm,alpha=1.0,shading='auto',edgecolors='none')
      except:
         cmap = plt.get_cmap(colormap)
         norm = matplotlib.colors.BoundaryNorm(contours, ncolors=cmap.N, clip=True)
         #print('JDL MAX =',np.amax(model_output[0]))
         #print('JDL MIN =',np.amin(model_output[0]))
         if varname == 'paintball':
            #for nen in range(0,model_output.shape[0],5):#4):
            #   CS = plt.contourf(xx,yy,model_output[nen],cmap=cmap,norm=norm,alpha=0.25,shading='auto')#,edgecolors='none')
            for mindex,nen in enumerate(range(0,model_output.shape[0],10)):#4):
               #CS = plt.pcolormesh(xx,yy,model_output[nen],cmap=cmap,norm=norm,alpha=0.25,shading='auto')#,edgecolors='none')   
               tmp = np.where(np.isnan(model_output[nen]),np.nan,mindex)+1
               #CS = plt.contourf(xx,yy,model_output[nen],cmap=cmap,norm=norm,alpha=0.25,shading='auto')#,edgecolors='none')   
               print('MINDEX = ',mindex)
               print('tmp mean = ',np.nanmean(tmp))
               CS = plt.pcolor(xx,yy,tmp,cmap=cmap,norm=norm,alpha=0.3,shading='auto',edgecolors='none',snap='True')   
         elif varname == 'vpert1':
            CS = plt.pcolor(xx,yy,model_output,cmap=cmap,norm=norm,alpha=0.5,shading='auto',edgecolors='none',snap='True')
         else:
            CS = plt.pcolormesh(xx,yy,model_output,cmap=cmap,norm=norm,alpha=1.0,shading='auto',edgecolors='none')
   else: # contourf
      CS = plt.contourf(model_output, contours, colors = colormap,extend='both')

   if varname != 'JUNK': #'paintball':
      CB = plt.colorbar(CS, shrink=0.8, ticks = cb_ticks)
      if varname == 'vpert1':
        CB.set_label('Perturbation V (m s$^{-1}$) at 1 km AGL')
   #--- Plotting Single Contour Overlay
   if 'contour_output' in kwargs:
      if 'grdbas_obs' in kwargs:
         if HOV: # --- Hovmoeller Diagram
            xx_obs,yy_obs = np.meshgrid(kwargs['grdbas_obs'].th[:],kwargs['grdbas_obs'].yh[:])
         else:
            xx_obs,yy_obs = np.meshgrid(kwargs['grdbas_obs'].xh[:],kwargs['grdbas_obs'].yh[:])
      else:
         xx_obs = xx
         yy_obs = yy

      if 'contours' in kwargs:
         #pass
         plt.contour(xx_obs,yy_obs,kwargs['contour_output'],kwargs['contours'],linewidths=[2.0],colors=['k'])
      elif 'contour_var' in kwargs:
         if kwargs['contour_var'] in ['dbz']:
            plt.contour(xx_obs,yy_obs,kwargs['contour_output'],[25.0],linewidths=[2.0],colors=['#000000'])#'orangered']) #['#000000'])
         elif kwargs['contour_var'] in ['uh']:
            plt.contour(xx_obs,yy_obs,kwargs['contour_output'],[250.0],linewidths=[2.0],colors=['#000000'])
         elif kwargs['contour_var'] in ['w']:
            plt.contour(xx_obs,yy_obs,kwargs['contour_output'],[5.0],linewidths=[2.0],colors=['#000000'])


   #---Secondary Plotting (i.e., plotting specific points, polygons, etc.)
   if 'xpt' in kwargs:
      if polygon:
         x1 = kwargs['xpt'][0]
         x2 = kwargs['xpt'][0]
         x3 = kwargs['xpt'][1]
         x4 = kwargs['xpt'][1]
         y1 = kwargs['ypt'][0]
         y2 = kwargs['ypt'][1]
         y3 = kwargs['ypt'][1]
         y4 = kwargs['ypt'][0]
         poly = Polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)],facecolor='None',edgecolor='black',linewidth=3)
         plt.gca().add_patch(poly)
      else:
         num_points = len(kwargs['xpt'])
         for index in range(0,num_points):
            plt.plot(kwargs['xpt'][index],kwargs['ypt'][index],'*',markerfacecolor='w',markersize=25.,markeredgecolor='k')
   if 'xpt_dis' in kwargs:
      if polygon:
         x1 = kwargs['xpt_dis'][0]
         x2 = kwargs['xpt_dis'][0]
         x3 = kwargs['xpt_dis'][1]
         x4 = kwargs['xpt_dis'][1]
         y1 = kwargs['ypt_dis'][0]
         y2 = kwargs['ypt_dis'][1]
         y3 = kwargs['ypt_dis'][1]
         y4 = kwargs['ypt_dis'][0]
         poly = Polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)],facecolor='None',edgecolor='black',linewidth=3)
         plt.gca().add_patch(poly)
      else:
         num_points = len(kwargs['xpt_dis'])
         for index in range(0,num_points):
            if num_points > 50:
               plt.plot(kwargs['xpt_dis'][index],kwargs['ypt_dis'][index],'*',markerfacecolor='r',markersize=5.,markeredgecolor='r')
            else:
               plt.plot(kwargs['xpt_dis'][index],kwargs['ypt_dis'][index],'*',markerfacecolor='w',markersize=25.,markeredgecolor='k')
           
   if 'linex' in kwargs:
      x0 = kwargs['linex'][0]
      x1 = kwargs['linex'][1]
      y0 = kwargs['liney'][0]
      y1 = kwargs['liney'][1]
      plt.plot(kwargs['linex'][:],kwargs['liney'][:],linestyle='--',linewidth=2.0,color='#E50000')

  
   plt.xlim([np.amin(xx),np.amax(xx)])
   #plt.ylim([np.amin(yy),np.amax(yy)])
 
   #--- Final Touches (title, saving figure) 
   if 'title' in kwargs:
      plt.title(kwargs['title'])
   if 'outpath' in kwargs:
      print('Saving to ... ',kwargs['outpath'])
      #figure = plt.gcf()
      #figure.set_size_inches(13, 13)
      if (grdbas.xmax - grdbas.xmin > 1) & (grdbas.ymax-grdbas.ymin > 1):
         ax.set_aspect('equal')
      #plt.axes().set_aspect('equal')
      plt.tight_layout()
      plt.tick_params(axis='both',length=5,width=1.)
      plt.savefig(kwargs['outpath'], dpi=300)#,figsize=(13,13))
   else: 
      plt.show()

  
def plotVar_multiplot(model_output,varname,pcolor = True, HOV = False, **kwargs):
   """
   Goal: Plot horizontal cross sections of model variables on the figure

   #--- Overall Figure
   grdbas:          object
   figure:          object  #--- Currently made in the program, not passed in


   #--- Multiplot features
   axs = figure plots
   pindex = picture index (which picture is plotted)?

   #--- Original Figure
   var:             string
   outpath:         string
   model_output:    [ny,nx] matrix
   title            string

   #--- Contouring
   grdbas_obs:      A seperate gridbase file if observations are on different grid 
                    from model output
   contour_output:  [ny,nx] matrix
   contour_var:     string
   contours   :     array of contouring values

   #--- Plotting Point Plots (Currently Incapable)
   lat:             list
   lon:             list
   MPing:           list
   xpt              list
   ypt              list

   Required arguments:
      var: The Variable name (String)
      model_output: The model variable being contoured
   """

  #--- Making Figure (either pcolor or contourf)
   contours,cb_ticks,colormap = post.plot.colormaps.define_contours(varname)
   #--- Plotting Dimensions
   if 'grdbas' in kwargs:
      #plt.ylabel('Distance (km)')
      if HOV: # --- Hovmoeller Diagram
         xx,yy = np.meshgrid(kwargs['grdbas'].th[:],kwargs['grdbas'].yh[:])
      #   #plt.xlabel('Time (s)')
      else:
         xx,yy = np.meshgrid(kwargs['grdbas'].xh[:],kwargs['grdbas'].yh[:])


         #plt.xlabel('Distance (km)')
   else:
      [ny,nx] = model_output.shape
      xx,yy = np.meshgrid(np.arange(0,nx),np.arange(0,ny))

   #--- Deteriming the location where plot is placed
   if 'axs' in kwargs:
      axs = kwargs['axs']
      if 'pindex' in kwargs:
         pindex = kwargs['pindex']
      else:
         pindex = 0
      try:
         if axs.ndim > 1:
            [ny,nx] = axs.shape
            pindex_x = pindex%nx
            pindex_y = int(np.ceil(float(pindex)/float(nx))) - 1
         else:
            pindex_x = pindex
      except:
         pindex_x = 0
         pindex_y = 0


   #--- Plotting via Pcolormesh
   if pcolor:
      cmap = matplotlib.colors.ListedColormap(colormap,cb_ticks)
      norm = matplotlib.colors.BoundaryNorm(contours,ncolors=len(colormap),clip=True)
      try:
         CS = axs[pindex_y,pindex_x].pcolormesh(xx,yy,model_output,cmap=cmap,norm=norm,alpha=0.8,shading='auto')
      except:
         try:
            CS = axs[pindex_x].pcolormesh(xx,yy,model_output,cmap=cmap,norm=norm,alpha=0.8,shading='auto')
         except:
            CS = plt.pcolormesh(xx,yy,model_output,cmap=cmap,norm=norm,alpha=0.8,shading='auto')

   #--- Plotting via contourf
   else: 
      try:
         CS = axs[pindex_y,pindex_x].contourf(model_output, contours, colors = colormap,extend='both')
      except:
         try:
            CS = axs[pindex_x].contourf(model_output, contours, colors = colormap,extend='both')
         except:
            CS = plt.contourf(model_output, contours, colors = colormap,extend='both')


   #--- Colorbar   
   try:
      if pindex == 0:
         plt.colorbar(CS, ax=axs[:, :], location='right', shrink=0.6)
   except:
      plt.colorbar(CS, shrink=0.8, ticks = cb_ticks) 


   #--- Overlay Contours
   #--- grdbas_obs allows observations to be plotted when they are on a different grid than model output
   if 'contour_output' in kwargs:
      if 'grdbas_obs' in kwargs:
         if HOV: # --- Hovmoeller Diagram
            xx_obs,yy_obs = np.meshgrid(kwargs['grdbas_obs'].th[:],kwargs['grdbas_obs'].yh[:])
         else:
            xx_obs,yy_obs = np.meshgrid(kwargs['grdbas_obs'].xh[:],kwargs['grdbas_obs'].yh[:])
      else:
         xx_obs = xx
         yy_obs = yy

      if 'contours' in kwargs:
         try:
            axs[pindex_y,pindex_x].contour(xx_obs,yy_obs,kwargs['contour_output'],kwargs['contours'],linewidths=[2.0],colors=['#000000'])
         except:
            try:
               axs[pindex_x].contour(xx_obs,yy_obs,kwargs['contour_output'],kwargs['contours'],linewidths=[2.0],colors=['#000000'])
            except:
               axs.contour(xx_obs,yy_obs,kwargs['contour_output'],kwargs['contours'],linewidths=[2.0],colors=['#000000'])


      #--- Contouring based upon other variables
      elif 'contour_var' in kwargs:
         if kwargs['contour_var'] in ['dbz']:
            try:
               axs[pindex_y,pindex_x].contour(xx_obs,yy_obs,kwargs['contour_output'],[25.0],linewidths=[2.0],colors=['#000000'])
            except:
               try:
                  axs[pindex_x].contour(xx_obs,yy_obs,kwargs['contour_output'],[25.0],linewidths=[2.0],colors=['#000000'])
               except:
                  print('JDL made it here!!!!')
                  plt.contour(xx_obs,yy_obs,kwargs['contour_output'],[25.0],linewidths=[2.0],colors=['#000000'])
		  #plt.contour(xx_obs,yy_obs,kwargs['contour_output'],[25.0],linewidths=[2.0],colors=['#000000'])

         elif kwargs['contour_var'] in ['uh']:
            if np.amax(kwargs['contour_output'])>75.0:
               try:
                  axs[pindex_y,pindex_x].contour(xx_obs,yy_obs,kwargs['contour_output'],[75.0],linewidths=[2.0],colors=['#000000'])
               except:
                  try:
                      axs[pindex_x].contour(xx_obs,yy_obs,kwargs['contour_output'],[75.0],linewidths=[2.0],colors=['#000000'])
   	              #axs[pindex_x].contour(xx_obs,yy_obs,kwargs['contour_output'],[75.0],linewidths=[2.0],colors=['#000000'])
                  except:
                     plt.contour(xx_obs,yy_obs,kwargs['contour_output'],[75.0],linewidths=[2.0],colors=['#000000'])
            else:
               print('NO CONTOURS')
         elif kwargs['contour_var'] in ['w','winterp']:
            try:
               axs[pindex_y,pindex_x].contour(xx_obs,yy_obs,kwargs['contour_output'],[1.0],linewidths=[2.0],colors=['#000000'])
            except:
               try:
                  axs[pindex_x].contour(xx_obs,yy_obs,kwargs['contour_output'],[1.0],linewidths=[2.0],colors=['#000000'])
               except:
                  plt.contour(xx_obs,yy_obs,kwargs['contour_output'],[1.0],linewidths=[2.0],colors=['#000000'])
               

   #--- Plot Titles
   if 'title' in kwargs:
      try:
         axs[pindex_y,pindex_x].set_title(kwargs['title'])
      except:
         try:
            axs[pindex_x].set_title(kwargs['title'])
         except:
            plt.title(kwargs['title'])
   #else: 

      #if HOV:
      #   axs[pindex_y,pindex_x].set_title('Hovmoeller of %s'%varname)
      #else:
      #   if 'contour_var' in kwargs:
      #      axs[pindex_y,pindex_x].set_title('%s with %s overlaid'%(varname,kwargs['contour_var']))
      #   else:
      #      pass
      #      #axs[pindex_x].set_title(varname)
   if 'zmin' in kwargs:
      try:
         axs[pindex_y,pindex_x].set_ylim(kwargs['zmin'],kwargs['zmax'])
      except:
         try:
             axs[pindex_x].set_ylim(kwargs['zmin'],kwargs['zmax'])
         except:
             plt.ylim(kwargs['zmin'],kwargs['zmax'])


def plotReliability(sample_climo,no_skill,obs_frequency,bin_centers,bin_climo,plot_bckd=True,**kwargs):
   """
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Goal:  Plot standard variables Reliability Curve
   !
   ! Need:  All of the data obtained from Reliability
   ! 
   !  kwargs:
   !     - label - Provide a label for the line
   !     - outpath - save the picture
   ! 
   !
   ! Produced June 9, 2015
   ! Author: Jon Labriola
   !
   ! Modifications: NONE
   !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   """


   #plt.figure()

   plt.xticks(np.arange(0.0, 1.2, 0.2))
   plt.yticks(np.arange(0.0, 1.2, 0.2))

   plt.axis([0., 1., 0., 1.])
   if 'linecolor' in kwargs:
     linecolor = kwargs['linecolor']
   else:
     linecolor = 'black'

   if plot_bckd:
      #Need sample_climo, no_skill
      plt.fill_between(np.arange(0, 1.001, 0.001), no_skill, np.ones((1001)), where=no_skill>sample_climo, edgecolor='#CCCCCC', facecolor='#CCCCCC', interpolate=True)
      plt.fill_between(np.arange(0, 1.001, 0.001), np.zeros((1001)), no_skill, where=no_skill<sample_climo, edgecolor='#CCCCCC', facecolor='#CCCCCC', interpolate=True)
   

      #Perfect reliability line
      #Need bin_centers
      plt.plot(bin_centers, bin_centers, color='#000000', linewidth=1.5, linestyle='--')

      #No resolution line (sample climatology)
      #bin_climo and bin_centers
      plt.plot(bin_centers, bin_climo, color='#000000', linewidth=1.5, linestyle='--')

   #Need obs_frequency
   frequency_masked = np.ma.masked_where(obs_frequency < 0, obs_frequency)

   #--- Plotting
   if 'label' in kwargs:
      plt.plot(bin_centers, frequency_masked, color = linecolor, linewidth = 5.0,label=kwargs['label'])
   else:
      plt.plot(bin_centers, frequency_masked, color = linecolor, linewidth = 5.0) #label = 'ROC= '+'%.3f'%ROC)




   if 'outpath' in kwargs:
     print("Plot saved to " + str(kwargs['outpath']))
     plt.savefig(kwargs['outpath'], figsize = (13, 13), dpi=300)
     plt.clf()

def gen_performance():
   """
   This function can be used to generate a simple performance diagram.
   Once the diaggram is created you can add your own FOH/POD pairs

   Required Inputs:
      None

   Returns: Figure Object to be used for plotting
   """
   figure = plt.figure(figsize=(14,11))
   x=y= np.arange(0,1.1,.01)
   X,Y = np.meshgrid(x,y)
   CSI = ((1/X)+(1/Y)-1)**-1
   #CS = plt.contourf(X,Y,CSI,np.arange(0.1,1.2,.2),colors=['#ffe6e6','#ff9999','#ff6666','#ff3333','#cc0000'])
   CS = plt.contourf(X,Y,CSI,np.arange(0.1,1.2,.2),colors=['#bfbfbf','#a6a6a6','#8c8c8c','#737373','#595959'])
   #CS = plt.contourf(X,Y,CSI,np.arange(0.1,1.2,.2),colors=['#80dfff','#4dd2ff','#1ac6ff','#00ace6','#0086b3'],alpha=0.5)
   #CS = plt.contourf(X,Y,CSI,np.arange(0.1,1.2,.2),colors=['#4db8ff','#1aa3ff','#008ae6','#006bb3','#004d80'],alpha=0.8)
   #CS = plt.contourf(X,Y,CSI,np.arange(0.1,1.2,.2),colors=['#8cd98c','#66cc66','#40bf40','#339933','#267326'],alpha=0.8)
   biases = [0.25,0.7,1,1.5,4]
   for i in biases:
      plt.annotate('%.2f'%i,(.5,.5*i),fontsize=10)
   Bias = Y/X
   BS = plt.contour(X,Y,Bias,biases,colors='black',linestyles='--')
   CB = plt.colorbar(CS, shrink=0.8, ticks = [0.1,0.3,0.5,0.7,0.9])
   CB.set_label('Critical Success Index')
   plt.xlim([0,1])
   plt.ylim([0,1])
   return figure
