import sys
import numpy as np
from numpy.fft import fft2, ifft2, fft, ifft
from operator import itemgetter, attrgetter
import Image
from math import *
import math

# Prend en argument un fichier Signal-bitscope-DATA.log

try:
    sys.argv[1]
except NameError:
    startingpoint = 'Missing an arg'
else:
    startingpoint = sys.argv[1]

Tableau = []
BaseData = []
DECIMATION = 1 	# Should we do a basic summation on the pixels, hence reducing the noice and the size of the picture?
BigPulseV = 2.0	# Seuil pour compter le pulse de position
DecPulse = 5 #
BaseDataDec = []
Tableau = []
k=0
BaseTime = startingpoint.split('-', 2 )


#Resetting the table
Tableau=[]
# Opening actual data
with open(startingpoint, 'r') as echOpenLog:
	for line in echOpenLog:
		k=k+1
		line = line.split('\t')
		del line[-1]
		Tableau.append(line)
SortedTable = np.array(Tableau).astype(float)
PointsPerLine = len(SortedTable[0])
NbOfLines = len(SortedTable)


# Debugging the image creation
print PointsPerLine 	# 2100
print NbOfLines 	# 120
# on retire les retards par ligne


# Creation de l'image
outfile = startingpoint +"-sorted.png"
NbSamples = 0
MeanZone = int(0)
MaxSignal = 0.00001


for i in range(NbOfLines):
    for j in range(PointsPerLine):
	if (j>800 and j<990):
	    MeanZone += SortedTable[i][j]
	    NbSamples += 1
	if (j>140 and j < 700):
	    if (SortedTable[i][j]>MaxSignal):
		MaxSignal = SortedTable[i][j]

MeanZone = MeanZone/NbSamples
SortedTable = (SortedTable-MeanZone*0.8) # Removing all information
SortedTable = np.array(SortedTable).astype(float)

# On normalise les donnees
MaxSignal = MaxSignal/1.76 # To get interesting signals from there
SortedTable = 0.99*(SortedTable*16.0/MaxSignal)
SortedTable = np.square(SortedTable)
SortedTable = np.square(SortedTable)
SortedTable = np.array(SortedTable).astype(int)

#SortedTable = np.sqrt(np.abs(SortedTable)) * np.sign(SortedTable) * 128




for i in range(NbOfLines):
    SortedTable[i][0] = 0
    SortedTable[i][1] = 0
    for j in range(PointsPerLine):
	if (j>519 and j<545):
		SortedTable[i][0] = SortedTable[i][0] + SortedTable[i][j]
	if (j>550 and j<610):
		SortedTable[i][0] = SortedTable[i][0] + SortedTable[i][j]
    print SortedTable[i][j]/24
SortedTable = SortedTable[np.argsort(SortedTable[:,0])]

# On recontrsuit l'image pour la sauver
Depth = PointsPerLine
size = (570,(int)(Depth/((1.0*DECIMATION)))) # fond du verre
ImagePoints=np.zeros(shape=(NbOfLines,Depth/DECIMATION))


# Creation d'une image non scan-converted
im = Image.new('RGB',size)
pix = im.load()


#Boucles
for i in range(size[0]): # les lignes
    for j in range(size[1]):
	value = SortedTable[NbOfLines-i-1][j]
	tmp = (int)(value/64)
        pix[i,j] = (tmp,tmp,tmp)

# Saving the image
im.save(outfile)


