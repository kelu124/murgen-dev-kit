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
from scipy.signal import hilbert, chirp


fs = 100e6 #sampling frequency in (samples/second)
ss = 1540 #speed of sound in tissue (m/s)
tf = 5e6 #transducer frequency (Hz)
sampleSize = 20000 #Total sample size (samples)
resolution = 0.25 #size of each data point (mm/column)
dne = 10 #millimeters between transducer camera and axis of rotation
a = 10*np.log10(2);

vmax = 0.5; #0.5, 10*np.log10(2) is max value
samp_end = 0; #number of samples at the end of the data to ignore
samp_front = 1000; #number of samples at the front of the data to ignore


zlength = np.round((1000)*(ss/fs)*(sampleSize)/2) #length in millimeters
sampleLength = zlength/sampleSize #size of each polar data point (mm/sample)
mm_front = dne + samp_front*sampleLength
mm_end = samp_end*sampleLength

def createCoordMap():
    null_cols = int(dne/resolution)    

    numberColumns = int(np.round(zlength/resolution) + null_cols)    #size of each rectangular data point
    numberRows = int(np.round(zlength/resolution)) #Since the angle swept by the transducer is 60 degrees, the geometry works out to make a square image.
    
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
    print len(rows)
    print len(columns)
    for r in range(0,len(rows)):
        for c in range(0,len(columns)):
            if(abs(coord_ang[r,c]) > 30): pass #No data beyond the angle sweep of the servo
            elif(coord_Rval[r,c] <= mm_front or coord_Rval[r,c] >= zlength-mm_end): pass
            else: data[r,c]=raw_data[round(coord_ang[r,c]+30),int(np.floor(coord_Rval[r,c]/sampleLength))]
    return data


datafile = sio.loadmat('bb_acq1.mat');    
signal_raw = np.array(datafile['echo_sig_cropped']).transpose();

baseline =  []
NbLines = len(signal_raw)
NbPtsPerLine = len(signal_raw[0])

def plotimg(data,cmap,z,zact,vmax,INVERT):
    if INVERT == True:
        plt.figure(); 
        plt.imshow(data, cmap = cmap, extent=[zact-z , zact, z/np.sqrt(3), -z/np.sqrt(3)], vmin = np.amin(data), vmax = np.amax(data)); plt.gca().invert_yaxis();
    elif INVERT == False:
        plt.figure();    
        plt.imshow(data, cmap = cmap, extent=[zact-z , zact, -z/np.sqrt(3), z/np.sqrt(3)], vmin = np.amin(data), vmax = np.amax(data))


fft = np.fft.fft2(signal_raw.transpose())



for i in range(1200):
	for j in (range(NbLines)):
		fft[i][j] = 1.0*i/1200*fft[i][j]
		fft[NbPtsPerLine-i-1][j] = 0

for i in range(8199):
	for j in (range(NbLines)):
		fft[1800+i][j] = 0
		fft[NbPtsPerLine-1800-i-1][j] = 0

spectre = abs(fft)
recontr = np.fft.ifft2(fft)

for i in range(2000):
	for j in (range(NbLines)):
		recontr[i][j] = 0

for i in range(NbPtsPerLine):
	for j in (range(NbLines)):
		recontr[i][j] = recontr[i][j]*(1+2.*np.exp(4.0*i/(1.2*NbPtsPerLine)))



recontr = abs(recontr**2)**(1.0/3.0)




#plotimg(spectre,cm.gray,7.7+zlength,zlength,np.max(spectre),True)
#plt.title('Processed Image')
plt.figure()
plt.plot(spectre[:NbPtsPerLine/2])
plt.grid()
plt.savefig('fooLucFiltered.png')

plt.figure()
#plt.plot(recontr)
plotimg(recontr.transpose(),cm.gray,7.7+zlength,8+zlength,np.max(recontr),False)
plt.title('Processed Image')
plt.grid()
plt.savefig('fooRecontr.png')


sio.savemat('cleaned.mat', {'echo_sig_cropped':recontr})
