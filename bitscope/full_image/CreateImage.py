import sys
import numpy as np
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
BigPulseV = 3.5	# Seuil pour compter le pulse de position

BaseTime = startingpoint.split('-', 2 )

# Opening the TimeStamp file
with open(BaseTime[0]+"-"+BaseTime[1]+"-"+"TimeStamp-bitscope-DATA.log",'r') as echOpenLog:
	for line in echOpenLog:
		line = line.split('\t')
		del line[-1]
		Tableau.append(line)
SortedTable = np.array(Tableau).astype(float)
PointsPerLine = len(SortedTable[0])
NbOfLines = len(SortedTable)
size = (NbOfLines,PointsPerLine)

for i in range(size[0]):
    value = 0
    for j in range(size[1]):
	if SortedTable[i][j] > BigPulseV:
		value=value+1
    BaseData.append(value)
#BaseData now contains the offset (ie position) of the transducer
MAAX = max(BaseData)

Tableau = []
# Opening actual data
with open(startingpoint, 'r') as echOpenLog:
	for line in echOpenLog:
		line = line.split('\t')
		del line[-1]
		Tableau.append(line)


SortedTable = 80*np.array(Tableau).astype(float)+1
SortedTable = (SortedTable**2)**(1/1.3)
#SortedTable = np.log(SortedTable)
SortedTable = np.array(SortedTable).astype(int)
PointsPerLine = len(SortedTable[0])
NbOfLines = len(SortedTable)

# Debugging the image creation
print PointsPerLine 	# 2100
print NbOfLines 	# 59

for i in range(NbOfLines):
    for j in range(PointsPerLine-MAAX):
	MaxLocal = BaseData[i]
	if j > PointsPerLine-MaxLocal:
		SortedTable[i][j] = 0
	else:
		SortedTable[i][j] = SortedTable[i][MaxLocal+j-1]
	if j == 0:
		SortedTable[i][j] = MaxLocal
print SortedTable

SortedTable = SortedTable[np.argsort(SortedTable[:,0])]

Depth = PointsPerLine-MAAX
size = (NbOfLines,Depth/(2*DECIMATION)) # retirer la deuxieme moitie
im = Image.new('RGB',size)
pix = im.load()
ImagePoints=np.zeros(shape=(NbOfLines,Depth/DECIMATION))

# Creation d'une image non scan-converted
for i in range(size[0]): # les lignes
    for j in range(size[1]):
	#value = 0
	for k in range(DECIMATION):
		value = SortedTable[i][j*DECIMATION+k]
	value = int(value)
	ImagePoints[i][j] = value
        pix[i,j] = (value,value,value) 

outfile = startingpoint +".png"
im.save(outfile)

# Doing a basic ScanConversion
X=np.zeros(shape=(size[0],size[1]))
Y=np.zeros(shape=(size[0],size[1]))
for i in range(size[0]):
    for j in range(size[1]):
	X[i][j] = j*math.cos(math.radians(i-30))
	Y[i][j] = ((size[1]+1)/2.0)+j*math.sin(math.radians(i-30))

MaxDepth = int(size[1]*math.cos(math.radians(30)))

sizeSC = (size[1],size[1])
ScanConverted=np.zeros(shape=(size[1],size[1]))
im = Image.new('RGB',(size[1],size[1]))
pix = im.load()
print sizeSC

#Creating the triangular image
for i in range(MaxDepth):
    if (i>1 & i<(size[1]-1)):
	    for j in range((size[1]/2-i/2),(size[1]/2+i/2)):
		D = (X-i)**2 + (Y-j)**2
		resul = np.unravel_index(D.argmin(), D.shape)
		# here is a basic NN, not even a 2-tap
		ScanConverted[i][j] = ImagePoints[resul[0]][resul[1]]

		value = int(ScanConverted[i][j])
		pix[j,i] = (value,value,value) 
outfile = startingpoint +"-SC.png"
im.save(outfile)
