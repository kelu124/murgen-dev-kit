import sys
import numpy as np
from numpy.fft import fft2, ifft2, fft, ifft
from operator import itemgetter, attrgetter
import Image
from math import *
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.io as sio
from scipy import signal
from scipy.signal import hilbert, chirp

# Prend en argument un fichier *.mat

try:
    sys.argv[1]
except NameError:
    startingpoint = 'Missing an arg'
else:
    startingpoint = sys.argv[1]

datafile = sio.loadmat(startingpoint);    
signal_raw = np.array(datafile['echo_sig_cropped']).transpose();

Tableau = []
# Opening actual data
k = 0
with open(startingpoint, 'r') as echOpenLog:
	for line in echOpenLog:
		k=k+1
		line = line.split('\t')
		del line[-1]
		Tableau.append(line)
SortedTable = signal_raw
PointsPerLine = len(SortedTable[0])
NbOfLines = len(SortedTable)

print PointsPerLine 	# 2100
print NbOfLines 	# 120

# Creation de l'image
outfile = startingpoint +".png"
NbSamples = 0
MeanZone = 0
MaxSignal = 0.00001

for i in range(NbOfLines):
    for j in range(PointsPerLine):
	if (j>PointsPerLine*0.2 and j<PointsPerLine*0.8):	# signal between 10% and 80%
	    MeanZone += SortedTable[i][j]
	    NbSamples += 1
	if (j>PointsPerLine*0.8):
	    if (SortedTable[i][j]>MaxSignal):
		MaxSignal = SortedTable[i][j]

MeanZone = MeanZone/NbSamples
SortedTable = (SortedTable - MeanZone) # Removing all information
SortedTable = np.array(SortedTable).astype(float)

# On normalise les donnees
MaxSignal = MaxSignal/1.05 # To get interesting signals from there
SortedTable = (SortedTable*16383.0/MaxSignal)
SortedTable = np.array(SortedTable).astype(int)


# On recontrsuit l'image pour la sauver
Depth = PointsPerLine
size = (NbOfLines,(int)(Depth)) # aller jusqu'au bocal
ImagePoints=np.zeros(shape=(NbOfLines,Depth))


# Creation d'une image non scan-converted
im = Image.new('RGB',size)
pix = im.load()

# Creation d'un fichier donnees
st = startingpoint+".csv"
targetFile = open(st, 'w')

#Boucles
for i in range(size[0]): # les lignes
    for j in range(size[1]):
	pix[i,j] = 128
	#value = 0
	value = SortedTable[i][j]
	tmp = abs((int)(value/64))
        pix[i,j] = (tmp,tmp,tmp)
	if(j==(size[1]-1)):
		targetFile.write(str(value))
	else:
		targetFile.write(str(value)+";")
    targetFile.write("\n")

targetFile.write("# More details:\n")
targetFile.write("#timestamp:"+str(startingpoint)+"\n")
targetFile.write("#lines:"+str(size[0])+"\n")
targetFile.write("#length:"+str(size[1])+"\n")
targetFile.write("#frequency:100000000\n")
targetFile.write("#piezofrequency:5000000\n")
targetFile.write("#angle:61\n")
targetFile.write("#anglestep:1\n")
targetFile.write("#apexoffset:10\n") # in mm
targetFile.write("# \n")
targetFile.write("# Data file created: from the murgen project \n")
targetFile.write("# Original log files: "+startingpoint+"\n")
targetFile.write("# See the tools at: https://github.com/kelu124/murgen-dev-kit/tree/master/software"+"\n")
targetFile.write("# \n")

# Saving the image
im.save(outfile)
# Closing the file
targetFile.close()

