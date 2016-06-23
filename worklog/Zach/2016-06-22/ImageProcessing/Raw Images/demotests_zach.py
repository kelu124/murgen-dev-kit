# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:01:32 2015

@author: caskeylab
"""

#demo of acquire_testdata and acquire_fulldata
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.io as sio
from matplotlib.colors import SymLogNorm

TESTDATA = 1;
FULLDATA = 2;

whichtest = TESTDATA; #type either TESTDATA or FULLDATA
print ("1");
def plotpolarimg(data,cmap,INVERT):
    if INVERT == True:
        plt.figure(); 
        plt.imshow(data, cmap = cmap, extent=[0, 20000, 60, 0], aspect='auto', norm=SymLogNorm(linthresh=3e-02, vmin=-1, vmax=1)); plt.gca().invert_yaxis();
    elif INVERT == False:
        plt.figure();    
        plt.imshow(data, cmap = cmap, extent=[0, 20000, 60, 0], aspect='auto', norm=SymLogNorm(linthresh=3e-02, vmin=-1, vmax=1))    
    plt.ylabel('angle theta')
    plt.xlabel('radius from transducer')

if whichtest == 1:
    datafile = sio.loadmat('C:/Users/OptLab/Desktop/Zach_Images/bb_acq1.mat');    
    timeaxis = np.array(datafile['timeaxis']);
    signal = np.array(datafile['echo_sig_cropped']).transpose();
    print(timeaxis,np.shape(signal))
    plt.plot(signal[30,:1000])
    
elif whichtest == 2:
    datafile = sio.loadmat('C:/Users/OptLab/Desktop/Zach_Images/bb_acq1.mat');    
    theta = np.array(datafile['theta_axis']);
    signal_raw = np.array(datafile['echo_sig_cropped'])
    print(signal_raw.shape)
    signal = signal_raw[1000:]
 
    filler = np.zeros([1000,61])

    signal1 = np.concatenate((filler, signal), axis=0)
    print(signal1.shape)
    signal1 = signal1.transpose()
    
  #  signal = signal.transpose()
  #  print(signal.shape, signal)
  #  print(np.amin(signal))
    
    plotpolarimg(signal.transpose(),cm.gray,True)
    plt.title('Plot of Raw Data')


    print(signal1.shape)