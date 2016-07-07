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
tf = 5e6 #transducer frequency (Hz)
sampleSize = 20000 #Total sample size (samples)
resolution = 0.25 #size of each data point (mm/column)
alpha = 0; # time gain compensation variable (if water = 0, tissue phantom = 0.5)
dne = 10 #millimeters between transducer camera and axis of rotation

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
    
def mapData(raw_data, coord_Rval, coord_ang, rows, columns, tf, alpha):
    data = np.empty([len(rows),len(columns)])
    
    if alpha != 0:    
        #use if at 5MHz and with tissue phantom: time gain compression    
        expvar = alpha*(tf/1e6)/(20*np.log10(np.e)); #5 stands for 5 MHz
        dog = np.exp(np.log(dog)+expvar*var_z/10); #zvalue needs to be in centimeters

    for r in range(0,len(rows)):
        for c in range(0,len(columns)):
            if(abs(coord_ang[r,c]) > 30): pass #No data beyond the angle sweep of the servo
            elif(coord_Rval[r,c]/sampleSize > 1): pass #Make the radius of the data uniform
            else: data[r,c]=raw_data[round(coord_ang[r,c]+30),np.floor(coord_Rval[r,c])]
    return abs(data) #Negatives are noise anyway
 
def plotimg(data,cmap,z,zact,INVERT):
    if INVERT == True:
        plt.figure(); 
        plt.imshow(data, cmap = cmap, extent=[zact-z , zact, z/np.sqrt(3), -z/np.sqrt(3)], aspect='auto', norm=SymLogNorm(linthresh=0.01, vmin=np.amin(data), vmax=np.amax(data))); plt.gca().invert_yaxis();
    elif INVERT == False:
        plt.figure();    
        plt.imshow(data, cmap = cmap, extent=[zact-z , zact, -z/np.sqrt(3), z/np.sqrt(3)], aspect='auto', norm=SymLogNorm(linthresh=0.01, vmin=np.amin(data), vmax=np.amax(data)))    
    plt.xlabel('mm in z-direction')
    plt.ylabel('mm in x-direction')
    
datafile = sio.loadmat('C:/Users/OptLab/Desktop/Zach_Images/bb_acq1.mat');    
signal_raw = np.array(datafile['echo_sig_cropped']);
signal = signal_raw[1000:]

filler = np.zeros([1000,61])
signal1 = np.concatenate((filler, signal), axis=0) #Replace pulse echo with zeros.

Rval, ang, rows, columns, zlength = createCoordMap()
data = mapData(signal1.transpose(), Rval, ang, rows, columns, tf, alpha)

plotimg(data,cm.gray,7.7+zlength,zlength,True)
plt.title('Plot of My Converted Data')
