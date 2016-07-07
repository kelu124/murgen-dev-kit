# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:53:24 2015

@author: caskeylab
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.io as sio
from scipy import signal

fs = 100e6 #sampling frequency in (samples/second)
ss = 1540 #speed of sound in tissue (m/s)
tf = 5e6 #transducer frequency (Hz)
sampleSize = 20000 #Total sample size (samples)
resolution = 0.25 #size of each data point (mm/column)
dne = 10 #millimeters between transducer camera and axis of rotation
a = 10*np.log10(2);
vmax = 0.5; #0.5, 10*np.log10(2) is max value
samp_end = 0; #number of samples at the end of the data to ignore
samp_front = 0; #number of samples at the front of the data to ignore


zlength = np.round((1000)*(ss/fs)*(sampleSize)/2) #length in millimeters
sampleLength = zlength/sampleSize #size of each polar data point (mm/sample)
mm_front = dne + samp_front*sampleLength
mm_end = samp_end*sampleLength

def createCoordMap():
    null_cols = int(dne/resolution)    

    numberColumns = np.round(zlength/resolution) + null_cols    #size of each rectangular data point
    numberRows = np.round(zlength/resolution) #Since the angle swept by the transducer is 60 degrees, the geometry works out to make a square image.
    
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
    
    
    return coord_Rval, coord_ang, rows, columns, zlength
    
def mapData(raw_data, coord_Rval, coord_ang, rows, columns, tf):
    data = np.empty([len(rows),len(columns)])
    
    for r in range(0,len(rows)):
        for c in range(0,len(columns)):
            if(abs(coord_ang[r,c]) > 30): pass #No data beyond the angle sweep of the servo
            elif(coord_Rval[r,c] <= mm_front or coord_Rval[r,c] >= zlength-mm_end): pass
            else: data[r,c]=raw_data[round(coord_ang[r,c]+30),np.floor(coord_Rval[r,c]/sampleLength)]
    return data
 
def plotimg(data,cmap,z,zact,vmax,INVERT):
    if INVERT == True:
        plt.figure(); 
        plt.imshow(data, cmap = cmap, extent=[zact-z , zact, z/np.sqrt(3), -z/np.sqrt(3)], vmin = np.amin(data), vmax = np.amax(data)); plt.gca().invert_yaxis();
    elif INVERT == False:
        plt.figure();    
        plt.imshow(data, cmap = cmap, extent=[zact-z , zact, -z/np.sqrt(3), z/np.sqrt(3)], vmin = np.amin(data), vmax = np.amax(data))
        
    plt.xlabel('mm in z-direction')
    plt.ylabel('mm in x-direction')

def butter_bandpass(lowcut, highcut, fs, order=3):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='bandpass', analog = False)
    return b, a   

def butter_highpass(cutoff, fs, order=3):
    nyq = 0.5*fs
    co = cutoff/nyq
    b, a = signal.butter(order,co,btype = 'highpass', analog = False)
    return b, a
    
def downmixing(signal_rf,fdemod, fs):
    b1, a1 = butter_highpass(fdemod/2,fs);    
    t = np.asarray(range(1,signal_rf.shape[1]+1))/fs;
    ee = np.exp(-1j*2*np.pi*fdemod*t);
    signal_iq = signal_rf*ee;
    signal_iqfilt = signal.filtfilt(b1,a1,signal_iq);
    signal_iqeng = signal_iqfilt*np.sqrt(2);
    len_dec = np.floor(signal_rf.shape[1]/10);
    signal_dec = np.zeros([61,len_dec], dtype = np.complex128)
    for x in range(0,int(len_dec)):
        signal_dec[:,x] = signal_iqeng[:,x*10]
    return signal_dec
    
def reconstruct(signal_dec,fdemod,fs):
    b1, a1 = butter_highpass(fdemod/2,fs);      
    len_dec = int(signal_dec.shape[1])
    signal_zerop = np.zeros([61,len_dec*10], dtype = np.complex128)    
    for x in range(0,len_dec):
        signal_zerop[:,x*10] = signal_dec[:,x];
    signal_zpfilt = signal.filtfilt(b1,a1,signal_zerop);
    r = np.asarray(range(1,(len_dec*10)+1))
    t = r/fs;    
    ee = np.exp(1j*2*np.pi*fdemod*t);
    signal_upmix = signal_zpfilt*ee;
    signal_recon = np.sqrt(2)*np.real(signal_upmix)    
    return signal_recon
    

b2, a2 = butter_bandpass(2.25e6,2.75e6,fs)
    
datafile = sio.loadmat('C:/Users/OptLab/Desktop/Zach_Images/bb_acq1.mat');    
signal_raw = np.array(datafile['echo_sig_cropped']).transpose();

butter1 = signal.filtfilt(b2,a2,signal_raw)
decimated = downmixing(butter1,tf,fs); 
reconstructed = reconstruct(decimated,tf,fs);
sig_env = abs(signal.hilbert(reconstructed));

Rval, ang, rows, columns, zlength = createCoordMap()
data = mapData(np.log10(sig_env), Rval, ang, rows, columns, tf)
print(np.amin(data),np.amax(data))
data = abs(data)
plotimg(data,cm.gray,7.7+zlength,zlength,vmax,True)
plt.title('Processed Image')