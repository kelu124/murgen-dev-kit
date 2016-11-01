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
    for j in range(PointsPerLine):
	if (j<30):
	    MeanZone += SortedTable[i][j]
	    NbSamples += 1
	if (j>350 and j < 700):
	    if (SortedTable[i][j]>MaxSignal):
		MaxSignal = SortedTable[i][j]

MeanZone = MeanZone*1.0/NbSamples
SortedTable = (SortedTable-MeanZone*0.9) # Removing all information
SortedTable = np.array(SortedTable).astype(float)

# On normalise les donnees
MaxSignal = MaxSignal/1.56 # To get interesting signals from there
SortedTable = 0.99*(SortedTable*256.0*64.0/MaxSignal)
SortedTable = np.array(SortedTable).astype(int)
SortedTable = np.sqrt(np.abs(SortedTable)) * 128
SortedTable = np.array(SortedTable).astype(int)


for j in range(NbOfLines):
	if (SortedTable[j][54] < 8000 and j>1): # detecte les retards au demarrage (decallage a 72)
		for k in (range(PointsPerLine-72)):
			SortedTable[j][k+45-3] = SortedTable[j][k+72]
		for k in range(44):
			SortedTable[j][k] = SortedTable[j-1][k]


## On trie les piezos
for j in range(NbOfLines):
	PremZone = 0.0001
	SecondeZone = 0.0001
	Ref = 0.0001
	for k in range(PointsPerLine):
		if (k<20):
			Ref = Ref + SortedTable[j][k]
		if (k>90 and k < 110):
			PremZone = PremZone + SortedTable[j][k]
		if (k<225 and k < 245):
			SecondeZone = SecondeZone + SortedTable[j][k]
	SortedTable[j][0]=int(20*(PremZone)/Ref)

UnsortedTable = SortedTable
SortedTable = SortedTable[np.argsort(SortedTable[:,0])]


PiezoDeux = np.zeros(shape=(1,PointsPerLine))
PiezoTrois = np.zeros(shape=(1,PointsPerLine))
PiezoUn = np.zeros(shape=(1,PointsPerLine))

for k in range(NbOfLines):
	if (k>50 and k < 250):
		PiezoUn=PiezoUn+SortedTable[k]
	if (k>350 and k < 550):
		PiezoDeux=PiezoDeux+SortedTable[k]
	if (k>700 and k < 950):
		PiezoTrois=PiezoTrois+SortedTable[k]

Coef=0.9
PiezoUn = Coef*PiezoUn/(250.0-50.0)
PiezoUnSquared = np.square(PiezoUn)
PiezoDeux = Coef*PiezoDeux/(550.0-350.0)
PiezoDeuxSquared = np.square(PiezoDeux)
PiezoTrois = Coef*PiezoTrois/(950.0-700.0)
PiezoTroisSquared = np.square(PiezoTrois)


for k in range(NbOfLines):
	t = np.square(UnsortedTable[k])	

	a = 0
	b = 0
	c = 0
	for i in range(300):
		#print i
		a = a+abs(t[i] - PiezoUnSquared[0][i])
		b = b+abs(t[i] - PiezoDeuxSquared[0][i])
		c = c+abs(t[i] - PiezoTroisSquared[0][i])

	if (a<b):
		if (b<c):
			UnsortedTable[k]=UnsortedTable[k]-PiezoUn
		elif (c<a):
			UnsortedTable[k]=UnsortedTable[k]-PiezoTrois
	else:
		if (b<c):
			UnsortedTable[k]=UnsortedTable[k]-PiezoDeux
		else:
			UnsortedTable[k]=UnsortedTable[k]-PiezoTrois

SortedTable = UnsortedTable

MaxSignal = 0.00001
MeanZone = 00000.1
NbSamples = 0
for i in range(NbOfLines):
    for j in range(PointsPerLine):
	if (j<30):
	    MeanZone += SortedTable[i][j]
	    NbSamples += 1
	if (j>160 and j < 450):
	    if (SortedTable[i][j]>MaxSignal):
		MaxSignal = SortedTable[i][j]

MeanZone = MeanZone*1.0/(NbSamples)
SortedTable = (SortedTable-MeanZone*0.9) # Removing all information
SortedTable = 3.0*np.array(SortedTable).astype(float)




# On recontrsuit l'image pour la sauver
Depth = PointsPerLine
size = (NbOfLines,(int)(Depth/((1.0*DECIMATION*3)))) # fond du verre
ImagePoints=np.zeros(shape=(NbOfLines,Depth/DECIMATION))


# Creation d'une image non scan-converted
im = Image.new('RGB',size)
pix = im.load()

# Creation d'un fichier donnees
st = BaseTime[0]+"-"+BaseTime[1]+".csv"
targetFile = open(st, 'w')
print "Writing file"
#Boucles
for i in range(size[0]): # les lignes
    for j in range(size[1]):
	value = SortedTable[i][j]
	tmp = (int)(value/64)
        pix[i,j] = (tmp,tmp,tmp)
	if(j==(size[1]-1)):
		targetFile.write(str(value))
	else:
		targetFile.write(str(value)+";")
    targetFile.write("\n")

targetFile.write("# More details:\n")
targetFile.write("#timestamp:"+str(BaseTime[0])+"-"+str(BaseTime[1])+"\n")
targetFile.write("#lines:"+str(size[0])+"\n")
targetFile.write("#length:"+str(size[1])+"\n")
targetFile.write("#frequency:5000000\n")
targetFile.write("#piezofrequency:3500000\n")
targetFile.write("#angle:60\n")
targetFile.write("#anglestep:0.5\n")
targetFile.write("# \n")
targetFile.write("# Data file created: from the murgen project \n")
targetFile.write("# Original log files: "+BaseTime[0]+"-"+BaseTime[1]+"\n")
targetFile.write("# See the tools at: https://github.com/kelu124/murgen-dev-kit/tree/master/software"+"\n")
targetFile.write("# Adapted in CSV format for Mehdi@echOpen : https://github.com/kelu124/murgen-dev-kit/tree/master/software/examples_CSV"+"\n")
targetFile.write("# \n")
  
# Saving the image
im.save(outfile)
# Closing the file
targetFile.close()

