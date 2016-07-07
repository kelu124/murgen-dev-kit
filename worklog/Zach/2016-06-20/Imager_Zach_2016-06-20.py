# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:31:02 2015

@author: caskeylab
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:53:24 2015

@author: caskeylab
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.io as sio
from matplotlib.colors import SymLogNorm

fs = 100e6 #sampling frequency in (samples/second)
ss = 1540 #speed of sound in tissue (m/s)
sampleSize = 20000 #Total sample size (samples)
resolution = 0.25 #size of each data point (mm/column)

def createCoordMap():
    zlength = np.round((1000)*(ss/fs)*(sampleSize)/2) #length in millimeters
    sampleLength = zlength/sampleSize #size of each polar data point
    numberColumns = np.round(zlength/resolution)    #size of each rectangular data point
    numberRows = numberColumns #Since the angle swept by the transducer is 60 degrees, the geometry works out to make a square image.
    
    center_r = np.ceil(numberRows/2); #finds middle row to use as zero
    
    rows = np.asarray(range(0,int(numberRows)))
    columns = np.asarray(range(0,int(numberColumns)))
    rows = rows-center_r

    coord_ang = np.zeros([numberRows,numberColumns])
    coord_Rval = np.zeros([numberRows,numberColumns])
    for r in range(0,len(rows)):
        for c in range(0,len(columns)):
            coord_Rval[r,c]= np.hypot(rows[r]*resolution,columns[c]*resolution) #Rval in millimeters
            coord_ang[r,c] = (np.arctan2(rows[r],columns[c]))*(180/np.pi) #angle in degrees
    coord_Rval = coord_Rval/sampleLength #Rval in sample number
    
    return coord_Rval, coord_ang, rows, columns, zlength
    
def mapData(raw_data, coord_Rval, coord_ang, rows, columns):
    data = np.empty([len(rows),len(columns)])
    for r in range(0,len(rows)):
        for c in range(0,len(columns)):
            if(abs(coord_ang[r,c]) > 30): pass #No data beyond the angle sweep of the servo
            elif(coord_Rval[r,c]/sampleSize > 1): pass #Make the radius of the data uniform
            else: data[r,c]=raw_data[round(coord_ang[r,c]+30),np.floor(coord_Rval[r,c])]
    return data #Negatives are noise anyway
 
def plotimg(data,cmap,z,zact,INVERT):
    if INVERT == True:
        plt.figure(); 
        plt.imshow(data, cmap = cmap, extent=[zact-z , zact, z/np.sqrt(3), -z/np.sqrt(3)], aspect='auto', norm=SymLogNorm(linthresh=0.01, vmin=np.amin(data), vmax=np.amax(data))); plt.gca().invert_yaxis();
    elif INVERT == False:
        plt.figure();    
        plt.imshow(data, cmap = cmap, extent=[zact-z , zact, -z/np.sqrt(3), z/np.sqrt(3)], aspect='auto', norm=SymLogNorm(linthresh=0.01, vmin=np.amin(data), vmax=np.amax(data)))    
    plt.xlabel('mm in z-direction')
    plt.ylabel('mm in x-direction')
    
datafile = sio.loadmat('first_acq_murgen.mat');    
signal_raw = np.array(datafile['echo_sig_cropped']);

signal = signal_raw[1000:] #Remove the pulse echo.
filler = np.zeros([1000,61])
signal1 = np.concatenate((filler, signal), axis=0) #Replace pulse echo with zeros.
signal1 = signal1.transpose()
    
Rval, ang, rows, columns, zlength = createCoordMap()
data = mapData(signal1, Rval, ang, rows, columns)

plotimg(data,cm.gray,7.7+zlength,zlength,True)
plt.title('Plot of My Converted Data')
