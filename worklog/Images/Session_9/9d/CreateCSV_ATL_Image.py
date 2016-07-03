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
outfile = startingpoint +".png"
NbSamples = 0
MeanZone = int(0)
MaxSignal = 0.00001
for i in range(NbOfLines):
    MeanZone = 0
    NbSamples = 0
    for j in range(PointsPerLine):
	if (j>275 and j < 700):
	    if (SortedTable[i][j]>MaxSignal):
		MaxSignal = SortedTable[i][j]
	    if (j>410 and j < 530):
	    	MeanZone += SortedTable[i][j]
	    	NbSamples = NbSamples+1
    MeanZone = MeanZone/NbSamples
    SortedTable[i] = SortedTable[i] - MeanZone


SortedTable = np.array(SortedTable).astype(float)

for i in range(NbOfLines):
	if (i>0 and i<(NbOfLines-2)):
		if SortedTable[i][49]<(SortedTable[i-1][49]+SortedTable[i+1][49])/4.0:
			for j in range(PointsPerLine-72):
			    SortedTable[i][j]=SortedTable[i][j+72-41]

## Premier tri a faire sur 770 a 842 
for i in range(NbOfLines):
    Category = 0
    for j in range(NbOfLines):
        if (j>775 and j<900):
	    Category = Category+SortedTable[i][j]
    Category = Category / 70.0
    SortedTable[i][-1] = Category
#SortedTable = SortedTable[np.argsort(SortedTable[:,-1])]


# On normalise les donnees
MaxSignal = MaxSignal/1.56 # To get interesting signals from there
SortedTable = 0.99*(SortedTable*256.0*64.0/MaxSignal)
SortedTable = np.array(SortedTable).astype(int)

SortedTable = np.sqrt(np.abs(SortedTable)) * 128

# On recontrsuit l'image pour la sauver
Depth = PointsPerLine
size = (NbOfLines,(int)(Depth/((1.0*DECIMATION)))) # fond du verre
ImagePoints=np.zeros(shape=(NbOfLines,Depth/DECIMATION))


# Creation d'une image non scan-converted
im = Image.new('RGB',size)
pix = im.load()

# Creation d'un fichier donnees
st = BaseTime[0]+"-"+BaseTime[1]+".csv"
print "Writing file"
#Boucles
for i in range(size[0]): # les lignes
    for j in range(size[1]):
	value = SortedTable[i][j]
	tmp = (int)(value/64)
        pix[i,j] = (tmp,tmp,tmp)
# Saving the image
im.save(outfile)
# Closing the file


