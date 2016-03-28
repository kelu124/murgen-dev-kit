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
BigPulseV = 2.5	# Seuil pour compter le pulse de position

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
k=0
# Opening actual data
with open(startingpoint, 'r') as echOpenLog:
	for line in echOpenLog:
		k=k+1
		line = line.split('\t')
		del line[-1]
		#if (k<60):		
		Tableau.append(line)


SortedTable = Tableau
PointsPerLine = len(SortedTable[0])
NbOfLines = len(SortedTable)

# Debugging the image creation
print PointsPerLine 	# 2100
print NbOfLines 	# 59
# on retire les retards par ligne
for i in range(NbOfLines):
    for j in range(PointsPerLine-MAAX):
	MaxLocal = BaseData[i]
	if j > PointsPerLine-MaxLocal:
		SortedTable[i][j] = 0
	else:
		SortedTable[i][j] = SortedTable[i][MaxLocal+j-1]
	if j == 0:
		SortedTable[i][j] = MaxLocal



SortedTable = np.array(SortedTable).astype(float)
NbSamples = 0
MeanZone = 0
MaxSignal = 0.00001
for i in range(NbOfLines):
    for j in range(PointsPerLine-MAAX):
	if (j>250/DECIMATION and j<270/DECIMATION):
	    MeanZone += SortedTable[i][j]
	    NbSamples += 1
	if (j>400/DECIMATION):
	    if (SortedTable[i][j]>MaxSignal):
		MaxSignal = SortedTable[i][j]

MeanZone = MeanZone/NbSamples
SortedTable = SortedTable - MeanZone
MaxSignal = MaxSignal/2.0
SortedTable = (SortedTable*16383/MaxSignal)
SortedTable = np.array(SortedTable).astype(int)
SortedTable = SortedTable[np.argsort(SortedTable[:,0])]
print SortedTable

print MeanZone
print MaxSignal
#Formatage
#SortedTable = 40*np.array(SortedTable).astype(float)+1
#SortedTable = (SortedTable**2)**(1/1.3)
#SortedTable = np.log(SortedTable)

# Trier les angles


# Refaire l'image
Depth = PointsPerLine-MAAX
size = (NbOfLines,(int)(Depth/((1.5*DECIMATION)))) # aller jusqu'au bocal
ImagePoints=np.zeros(shape=(NbOfLines,Depth/DECIMATION))
#Prepare the png image
im = Image.new('RGB',size)
pix = im.load()

st = BaseTime[0]+"-"+BaseTime[1]+".data"
targetFile = open(st, 'w')

	
# Creation d'une image non scan-converted
for i in range(size[0]): # les lignes
    for j in range(size[1]):
	#value = 0
	for k in range(DECIMATION):
		value = SortedTable[i][j*DECIMATION+k]
	value = int(value)
	tmp = (int)(value/64)
        pix[i,j] = (tmp,tmp,tmp) 
	targetFile.write(str(value)+"\t")

    targetFile.write("\n")

outfile = startingpoint +".png"
im.save(outfile)
targetFile.close()

# Doing a basic ScanConversion, on 120 lines images
if False: #comment
	X=np.zeros(shape=(size[0],size[1]))
	Y=np.zeros(shape=(size[0],size[1]))
	for i in range(size[0]):
	    for j in range(size[1]):
		X[i][j] = j*math.cos(math.radians(0.5*i-30)) #0.5 factor because 120*0.5 = 60 max in an out
		Y[i][j] = (size[1]+1)/2.0+j*math.sin(math.radians(0.5*(i)-30)) # same

	MaxDepth = int(size[1]*math.cos(math.radians(30)))

	sizeSC = (size[1],size[1])
	ScanConverted=np.zeros(shape=(size[1],size[1]))
	im = Image.new('RGB',(size[1],size[1]))
	pix = im.load()
	print sizeSC

	for i in range(MaxDepth):
	    if (i>1 & i<(size[1]-1)):
		    for j in range((size[1]/2-i/2),(size[1]/2+i/2)):
			D = (X-i)**2 + (Y-j)**2
			resul = np.unravel_index(D.argmin(), D.shape)
			# here is a basic NN, not even a 2-tap
			ScanConverted[i][j] = ImagePoints[resul[0]][resul[1]]

			value = int(ScanConverted[i][j])
			pix[j,i] = (value,value,value)
	    print i 
	outfile = startingpoint +"-SC.png"
	im.save(outfile)


