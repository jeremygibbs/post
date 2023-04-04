#!/usr/bin/env python2.7

#Author: Jon Labriola
#Written: Feb. 2015

#Purpose:  A suite of different verification method
#          Include Various Verification Methods including:
#          1.) NEP
#          2.) Reliability
#          3.) Probability Matched Meani
#from numpy import *
import numpy as np
from post.calc.misc import define_kernel
from scipy import signal as sg
from scipy.signal import convolve2d

def createNEP(ensemble,kernel_radius,threshold):
   """
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
   ! Goal: Convert an Ensemble of Data to an NEP 
   !       product.  Only looks at a single time
   !
   ! Need: Ensemble,Kernel Radius,Threshold
   ! Note: Ensemble Shape= [nen,ny,nx]
   !       prob_vals = [ny,nx] 
   ! 
   ! Produced May 12, 2015
   ! Author: Jon Labriola
   !
   ! Modifications: None
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   """
   kernel = define_kernel(kernel_radius)
   prob_vals = np.empty(ensemble[0,:,:].shape)
   neighborhood_ensemble = np.empty(ensemble.shape)
   for ens_mem in np.arange(1,len(ensemble[:,0,0]) , 1):
      neighborhood_ensemble[ens_mem] = sg.convolve2d(ensemble[ens_mem,:,:] > threshold, kernel, mode='same', boundary='symm')

   #Use some kind of python black magic to obtain NEP out of the convolution
   prob_vals = neighborhood_ensemble.sum(axis=0) / (neighborhood_ensemble.shape[0] * kernel.sum())
   return(prob_vals) 


def createMNEP(ensemble,kernel_radius,threshold):
   """
   Goal: Convert an Ensemble of Data to an MNEP product 
   Focuses on probability of event occuring within a 
   set distances.
   
   
   """
   kernel = define_kernel(kernel_radius)
   prob_vals = np.empty(ensemble[0,:,:].shape)


   ens_swath = pycaps.verify.ens_prob_within_dist(wind_torn_mask, threshold, kernel)

def createNMEP_single(member,kernel_radius,threshold):
   """ 
   Goal: Created NMEP but for a single member
   """
   kernel = define_kernel(kernel_radius)

   member_max = sg.convolve2d(member > threshold,kernel,mode='same',boundary='symm')
   member_max[member_max>0.0] = 1.0

   prob_mem = sg.convolve2d(member_max > 0, kernel, mode='same', boundary='symm')
   prob_mem = prob_mem/(kernel.sum())


   return(prob_mem)


def createNEP_Perc(ensemble,kernel_radius,threshold,perc=False,min_val=5.0):
   """
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Goal: Convert an Ensemble of Data to an NEP
   !       product.  Only looks at a single time
   !
   ! Need: Ensemble,Kernel Radius,Threshold
   ! Note: Ensemble Shape= [nen,ny,nx]
   !       prob_vals = [ny,nx]
   !
   ! Produced May 12, 2015
   ! Author: Jon Labriola
   !
   ! Modifications: None
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   """
   kernel = define_kernel(kernel_radius)
   prob_vals = np.empty(ensemble[0,:,:].shape)
   neighborhood_ensemble = np.empty(ensemble.shape)
   thresh_avg = 0.
   for ens_mem in np.arange(0,len(ensemble[:,0,0]) , 1):
      if perc == True:
        tmp_array = np.where(ensemble[ens_mem,:,:]<min_val,nan,ensemble[ens_mem,:,:])
        thresh_tmp = np.nanpercentile(tmp_array,threshold)
        thresh_avg += thresh_tmp
        neighborhood_ensemble[ens_mem] = sg.convolve2d(ensemble[ens_mem,:,:] > thresh_tmp, kernel, mode='same', boundary='symm')
      else:
        neighborhood_ensemble[ens_mem] = sg.convolve2d(ensemble[ens_mem,:,:] > threshold, kernel, mode='same', boundary='symm')

   if perc == True:
      print('Average Threshold = '+str(thresh_avg/float(ens_mem))) 
   
   #Use some kind of python black magic to obtain NEP out of the convolution
   prob_vals = neighborhood_ensemble.sum(axis=0) / (neighborhood_ensemble.shape[0] * kernel.sum())
   return(prob_vals)


def localThresh(fcst,kernel_radius,threshold):
   """
   Highlight points that exceed a maximum and put in a buffer of 
   kernel_radius 

   Requires: fcst, kernel_radius,threshold
   
   Returns: conv - The convolution array that 
                   
   """
   kernel = define_kernel(kernel_radius)
   conv = sg.convolve2d(fcst > threshold, kernel, mode='same', boundary='symm')
   return conv



def createReliability(NEP,obs,threshold,perc = False,min_val=5.0):
   """
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Goal:  Make a reliability curve 
   !        based upon selected swath of information
   !
   ! Need: NEP, Obs, Threshold
   ! Note: NEP/Obs Shape= [ny,nx]
   !       Threshold  = single val
   !
   ! Produced May 14, 2015
   ! Author: Jon Labriola
   !
   ! Modifications: None
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   """

   if perc == True:
     tmp = np.where(obs<min_val,nan,obs)
     thresh_tmp = np.nanpercentile(tmp,threshold)
     threshold = thresh_tmp
     print('Threshold= '+str(threshold))

   [ny,nx] = NEP.shape   
   xmin = 0
   ymin = 0
   xmax = nx
   ymax = ny

   bin_width = 0.05
   reliability_bins = np.arange(0.00, 1.00 + bin_width, bin_width)
   num_bins = len(reliability_bins) - 1
   
   #Reliability Diagram Variables
   obs_frequency = np.zeros((num_bins))
   bin_centers = np.zeros((num_bins))
   bin_count = np.zeros((num_bins)) 
  

   total_points = 0
   occur_points = 0
   for ix in np.arange(xmin, xmax, 1):
      for jy in np.arange(ymin, ymax, 1):
         total_points = total_points + 1
         #print obs.shape
         #print threshold
         if (obs[jy][ix] > threshold):
            occur_points = occur_points + 1
   
   obs_climo = float(occur_points) / float(total_points)
 
   for cur_bin in np.arange(0, num_bins, 1):
      samples = 0
      obs_yes = 0
      obs_no = 0

      #print 'calculating reliability for array of shape ' + str(NEP[xmin:xmax,ymin:ymax].shape)
      #print 'x: (' + str(xmin) + ':' + str(xmax) + ')   |   y: (' + str(ymin) + ':' + str(ymax) + ')'
      for i in np.arange(xmin, xmax, 1):
         for j in np.arange(ymin, ymax, 1):
            if( (NEP[j,i] >= reliability_bins[cur_bin]) and (NEP[j,i] <= reliability_bins[cur_bin + 1])):
               samples = samples + 1   #We found a forecast within the current bin
               if (obs[j,i] >= threshold):
                  obs_yes = obs_yes + 1 #The criteria was met in the obs. (positive observation)
               elif (obs[j,i] < threshold):
                  obs_no = obs_no + 1   #The criteria was not met in the obs. (negative observation)

      #Calculate observed frequency and center of forecast probability bin
      bin_centers[cur_bin] = (reliability_bins[cur_bin] + reliability_bins[cur_bin + 1]) / 2.0

      if(samples > 0):
         obs_frequency[cur_bin] = float(obs_yes) / float(obs_yes + obs_no)
      else:
         obs_frequency[cur_bin] = -999 #No samples -- no data!  Avoid divide-by-zero.
      bin_count[cur_bin] = samples

   #Sample climatology and no skill region
   sample_climo = np.zeros((1001))
   no_skill = np.zeros((1001))
   bin_climo = np.zeros((num_bins))

   for i in np.arange(0, num_bins, 1):
      bin_climo[i] = obs_climo

   for index, i in enumerate(np.arange(0, 1.001, 0.001)):
      sample_climo[index] = obs_climo
      no_skill[index] = 0.5 * (obs_climo + i)

   return sample_climo,no_skill,obs_frequency,bin_centers,bin_climo,reliability_bins,bin_count

def pmMean(var2D_ens):
   """  
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Goal:  Make the probability Matched Mean of
   !        an ensemble  quantity
   !
   ! Need: Ensemble Vals
   ! Note: Ens Shape= [n_ens,ny,nx,]
   !
   ! Produced June 5, 2015
   ! Author: Jon Labriola
   !
   ! Modifications: Flipped N_ens to be the first
   !                coordinate - Easier to put in
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   """

   n_ens = var2D_ens.shape[0]
   ny = var2D_ens.shape[1]
   nx = var2D_ens.shape[2]

   ensmean = np.mean(var2D_ens, axis=0) #Calculate ensemble mean

   all_values = []
   for jy in np.arange(0, ny):
      for ix in np.arange(0, nx):
         for member in np.arange(0, n_ens):
            all_values.append(var2D_ens[member, jy, ix])

   #Construct a tethered array to track where our ranked values are.
   tethered_array = np.zeros((ny, nx))
   for jy in np.arange(0, ny):
      for ix in np.arange(0, nx):
         tethered_array[jy, ix] = jy + (ny * ix)

   #Construct 1-D arrays to rank values
   ensmean_1d = []
   tethered_1d = []
   for jy in np.arange(0, ny):
      for ix in np.arange(0, nx):
         ensmean_1d.append(ensmean[jy, ix])
         tethered_1d.append(tethered_array[jy, ix])

   #Prepare the all_values array by sorting it from high to low:
   all_values.sort()
   all_values.reverse()

   #Tethering array eements to their position as tuples ensures the sort is reversible.
   position_tuples = list(zip(tethered_1d, ensmean_1d))
   #The lambda performs a "mini-function" -- google "python lambda notation" for info.
   sorted_tuples = sorted(position_tuples, key = lambda x: x[1])
   sorted_tuples.reverse()  #Put largest values first
   sorted_tuples = list(zip(*sorted_tuples))
   tethered_1d = sorted_tuples[0]
   ensmean_1d = sorted_tuples[1]

   pm_mean = np.zeros((ny, nx))

   for point in np.arange(0, nx*ny, 1):
      #The tethered array stores information on the position of the ranked points in ensmean.
      #We must first convert this data back into i- and j-locations, then assign the corresponding data.
      loc_jrank = np.mod(tethered_1d[point], ny)
      loc_irank = np.floor(int(tethered_1d[point] / ny))

      #print '********'
      #print '%s %s %s %s'%(loc_jrank, loc_irank, n_ens, point)

      pm_mean[int(loc_jrank), int(loc_irank)] = all_values[0 + int(n_ens * point)]

   return pm_mean

#--------------------------------------------------------------------#

def ROC(NEP,obs,threshold):
   """ 
   Calculate the Relative Operating Characteristic
   Requires: NEP,obs,threshold


   Returns: POD, POFD

   """
   probthresh = np.arange(0.00, 1.00, 0.01) #define your probability thresholds
   pod = np.zeros(len(probthresh) + 1)
   pofd = np.zeros(len(probthresh) + 1)  #False Alarm Rate

   #print 'Calculating the ROC'
   #print "Threshold", "POD", "FAR"

   for counter, curprob in enumerate(probthresh):  # Counter is 1,2,3,4... curprob = the probability threshold
      #fcst_yes = ma.masked_where(NEP < curprob, NEP) # Forecasted
      #fcst_no  = ma.masked_where(NEP >= curprob, NEP)

      fcst_yes = np.ma.masked_where(NEP < curprob, NEP) # Forecasted
      fcst_no  = np.ma.masked_where(NEP >= curprob, NEP)

      hit_array  = np.ma.masked_where(obs < threshold, fcst_yes)
      miss_array = np.ma.masked_where(obs < threshold, fcst_no)
      fa_array   = np.ma.masked_where(obs >= threshold, fcst_yes)
      cn_array   = np.ma.masked_where(obs >= threshold, fcst_no)

      #Calculate probability of detection (pod) and false alarm rate (far)
      #Total events = hits + misses
      #Total non-events = false alarms + correct nos

      hits = np.ma.count(hit_array)
      false_alarms = np.ma.count(fa_array)
      misses = np.ma.count(miss_array)
      correct_no = np.ma.count(cn_array)

      pod[counter] = float(hits) / float(hits + misses)    #Probability of detection: (hits) / (total events)
      pofd[counter] = float(false_alarms) / float(correct_no + false_alarms)

   return pod,pofd

#--------------------------------------------------------------------#

def AUC(NEP,obs,threshold):
   probthresh = np.arange(0.00, 1.00, 0.01) #define your probability thresholds
   pod = np.zeros(len(probthresh) + 1)
   pofd = np.zeros(len(probthresh) + 1)  #False Alarm Rate

   #print 'Calculating the ROC'
   #print "Threshold", "POD", "FAR"

   for counter, curprob in enumerate(probthresh):  # Counter is 1,2,3,4... curprob = the probability threshold
      #fcst_yes = ma.masked_where(NEP < curprob, NEP) # Forecasted 
      #fcst_no  = ma.masked_where(NEP >= curprob, NEP)
     
      fcst_yes = np.ma.masked_where(NEP < curprob, NEP) # Forecasted
      fcst_no  = np.ma.masked_where(NEP >= curprob, NEP)

      hit_array  = np.ma.masked_where(obs < threshold, fcst_yes)
      miss_array = np.ma.masked_where(obs < threshold, fcst_no)
      fa_array   = np.ma.masked_where(obs >= threshold, fcst_yes)
      cn_array   = np.ma.masked_where(obs >= threshold, fcst_no)

      #Calculate probability of detection (pod) and false alarm rate (far)
      #Total events = hits + misses
      #Total non-events = false alarms + correct nos

      hits = np.ma.count(hit_array)
      false_alarms = np.ma.count(fa_array)
      misses = np.ma.count(miss_array)
      correct_no = np.ma.count(cn_array)

      pod[counter] = float(hits) / float(hits + misses)    #Probability of detection: (hits) / (total events)
      pofd[counter] = float(false_alarms) / float(correct_no + false_alarms)  #Probability of false detection: (false alarms / total non-events)
      #print str(curprob), str(pod[counter]), str(pofd[counter])
   #print '----------'


#Now calculate AUC:
   AUC = -np.trapz(pod, pofd) #Area under curve using trapezoidal approximation.
   return AUC,pod,pofd

#--------------------------------------------------------------------#

def FSS(obs,fcst,threshold,square_width=20,**kwargs):
   """
   Calculates the Fractional Skill score for an ensmeble member
   obs and fcst have dimensions of [ny,nx]
   threshold is a float value

   Return:
      FSS: The fractional skill score at different size boxes
      climo:  The fraction of observations within the largest domain
   """

   FSS = np.zeros((square_width))
   obs = np.where(obs>threshold,1,0)
   fcst = np.where(fcst>threshold,1,0)

   if 'radius' in kwargs:
      kernel = define_kernel(kwargs['radius'])
      Area = float(kernel.sum()) 
      Pobs = convolve2d(obs, kernel, mode='same', boundary='symm')/float(kernel.sum())
      Pfcst = convolve2d(fcst, kernel, mode='same', boundary='symm')/float(kernel.sum())
      MSE = (1./float(Area)) *np.sum((Pobs-Pfcst)**2)
      MSE_REF = (1./float(Area))*(np.sum((Pobs**2)+(Pfcst**2)))
      FSS = 1-(MSE/MSE_REF)
      climo = np.mean(obs)
   else:
      for radius in np.arange(0,square_width):
         if radius == 0:
            Pobs = obs
            Pfcst = fcst
            Area = 1.0
         else:
            kernel = define_kernel(radius)
            Area = float(kernel.sum())
            Pobs = convolve2d(obs, kernel, mode='same', boundary='symm')/kernel.sum()
            Pfcst = convolve2d(fcst, kernel, mode='same', boundary='symm')/kernel.sum() 
         MSE = (1./float(Area)) *np.sum((Pobs-Pfcst)**2)
         MSE_REF = (1./float(Area))*(np.sum((Pobs**2)+(Pfcst**2)))
         FSS[radius] = 1-(MSE/MSE_REF)

      climo = np.mean(obs)
   return FSS,climo

#--------------------------------------------------------------------#


def BSS(NEP,obs,threshold):
   """
   Calculate the Briers Skill Score

   NEP = [ny x nx] Array
   obs = [ny x nx] Array
   threshold = Float

   return BSS (float)
   """


   [ny,nx] = obs.shape
   obs = np.where(obs>threshold,1,0)
   BS = np.mean((NEP - obs)**2)
   climo_freq = float(np.sum(obs))/float(ny*nx)
   BSref = np.mean((climo_freq - obs) **2)
   return 1- BS/float(BSref)

#--------------------------------------------------------------------#



#--------------------------------------------------------------------#

def contingency(fcst,obs,threshold):
   """
   Calculate contingency table values.
   obs and fcst have dimensions of [ny,nx]
   threshold is a double

   Return:
      a = correct hit
      b = False Alarm
      c = Miss
      d = correct negative
   """
   a = float(np.sum(np.where((fcst > threshold) & (obs > threshold),1,0)))  # Correct Hit
   b = float(np.sum(np.where((fcst > threshold) & (obs < threshold),1,0)))    # False Alarm
   c = float(np.sum(np.where((fcst < threshold) & (obs > threshold),1,0)))    # Miss
   d = float(np.sum(np.where((fcst < threshold) & (obs < threshold),1,0)))    # Correct Negative
   return a,b,c,d


#--------------------------------------------------------------------#

def performance_scores(fcst,obs,threshold,kernel=None):
   """
   Get the scores used to plot a performance diagram

   Required inputs:
         fcst:  Predicted field [ny,nx]
          obs:  Observed field  [ny,nx]
    threshold:  The value threshold to verify (float)

   Optional inpurs:
      kernel:  The kernel radius of influence for forecasts
               and observations. (Ignored if not specified)
   """
   a,b,c,d = contingency(fcst,obs,threshold)

   if a > 0 and b > 0:
      FOH  = float(a)/float(a+b)
   else:
      FOH = 0
   if a > 0 and c > 0:
      POD  = float(a)/float(a+c)
   else:
      POD = np.nan
   if a > 0 and b > 0 and c > 0:
      CSI  = float(a)/float(a+b+c)
   else:
      CSI = 0
   if a > 0 and c > 0:
      BIAS = float(a+b)/float(a+c)
   else:
      BIAS = 0
   return FOH,POD,CSI,BIAS

