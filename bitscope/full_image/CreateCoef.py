import os.path
import sys
import numpy as np
import Image
import math

#python
size = (30,1000) # because _30_ *2-1 is 59 lines, 1000 pixels deep at max

#Translating pixels in the rectangular shape to the polar coordinates equivalent
st = "/home/luc/murgen-dev-kit/bitscope/full_image/"
if(os.path.isfile(st+"X.pos")==0):
	targetFile = open(st+"X.pos", 'w')
	X=np.zeros(shape=(size[0],size[1]))
	for i in range(size[0]):
	    for j in range(size[1]):
		X[i][j] = j*math.cos(math.radians(i))
	for x in range(len(X)):
		for y in range(len(X[x])):
			targetFile.write(str(X[x][y])+"\t")
		targetFile.write("\n")
	targetFile.close()
else:
	X=[]
	with open(st+"X.pos",'r') as xCoef:
		for line in xCoef:
			line = line.split('\t')
			del line[-1]
			X.append(line)
	X = np.array(X).astype(float)
	print X
#Same thing for Y
if(os.path.isfile(st+"Y.pos")==0):
	targetFile = open(st+"Y.pos", 'w')
	Y=np.zeros(shape=(size[0],size[1]))
	for i in range(size[0]):
	    for j in range(size[1]):
		Y[i][j] = (j*math.sin(math.radians(i)))
	for x in range(len(Y)):
		for y in range(len(Y[x])):
			targetFile.write(str(Y[x][y])+"\t")
		targetFile.write("\n")
	targetFile.close()
else:
	Y=[]
	with open(st+"Y.pos",'r') as yCoef:
		for line in yCoef:
			line = line.split('\t')
			del line[-1]
			Y.append(line)
	Y = np.array(Y).astype(float)
	print Y

#Finding the nearest neighbour
ScanConvertParams=np.zeros(shape=(size[1],size[1]/2,3))
if(os.path.isfile(st+"NN.pos")==0):
	print "NN pos file does not exist yet"
	targetFile = open(st+"NN.pos", 'w')
	for i in range(size[1]):
	    for j in range(size[1]/2):
		if j==int(i/2):
			ScanConvertParams[i][j][0] = 1
			ScanConvertParams[i][j][1] = 0
			ScanConvertParams[i][j][2] = 0
		if (j<int(i/2)):
			D = (X-i)**2 + (Y-j)**2
			resul = np.unravel_index(D.argmin(), D.shape)
			# here is a basic NN, not even a 2-tap
			ScanConvertParams[i][j][0] = 1
			ScanConvertParams[i][j][1] = resul[0]
			ScanConvertParams[i][j][2] = resul[1]
	    print i

	for x in range(len(ScanConvertParams)):
		for y in range(len(ScanConvertParams[x])):
			for z in range(len(ScanConvertParams[x][y])):
				targetFile.write(str(ScanConvertParams[x][y][z])+"$")
			targetFile.write("\t")
		targetFile.write("\n")
	targetFile.close()
else:
	ScanConvertParams=[]
	print "NN pos file exists"
	with open(st+"NN.pos",'r') as NNCoef:
		for line in NNCoef:
			tmpTriplet = []
			line = line.split('\t')
			del line[-1]
			for triplet in line:
				triplet = triplet.split('$')
				del triplet[-1]
				tmpTriplet.append(triplet)
				## adding the 
			tmpTriplet = np.array(tmpTriplet).astype(float)
			ScanConvertParams.append(tmpTriplet) #adding a line of triplets
	ScanConvertParams = np.array(ScanConvertParams).astype(float)
#Checking for the lengths of the parameter	
print "Verification for NN ScanConvert Parameters"
print len(ScanConvertParams)
print len(ScanConvertParams[0])
print len(ScanConvertParams[0][0])


#Finding the four nearest neighbours
ScanConvert4TParams=np.zeros(shape=(size[1],size[1]/2,3*4))
if(os.path.isfile(st+"4T.pos")==0):
	print "4T pos file does not exist yet"
	targetFile = open(st+"4T.pos", 'w')
	for i in range(size[1]):
	    for j in range(size[1]/2):
		if j==int(i/2):
			for k in range(4):
				ScanConvert4TParams[i][j][k*3+0] = 1/4
				ScanConvert4TParams[i][j][k*3+1] = 0
				ScanConvert4TParams[i][j][k*3+2] = 0
		if (j<int(i/2)):
			D = (X-i)**2 + (Y-j)**2
			#Let's find the 4 nearest neighbours
			for k in range(4):
				resul = np.unravel_index(D.argmin(), D.shape)
				ScanConvert4TParams[i][j][k*3+0] = D[resul[0]][resul[1]]
				ScanConvert4TParams[i][j][k*3+1] = resul[0]
				ScanConvert4TParams[i][j][k*3+2] = resul[1]
				D[resul[0]][resul[1]]=1000000000
	    print i

	for x in range(len(ScanConvert4TParams)):
		for y in range(len(ScanConvert4TParams[x])):
			for z in range(len(ScanConvert4TParams[x][y])):
				targetFile.write(str(ScanConvert4TParams[x][y][z])+"$")
			targetFile.write("\t")
		targetFile.write("\n")
	targetFile.close()
else:
	ScanConvert4TParams=[]
	print "4T pos file exists"
	with open(st+"4T.pos",'r') as ftCoef:
		for line in ftCoef:
			tmpQuadTriplet = []
			line = line.split('\t')
			del line[-1]
			for QuadTriplet in line:
				QuadTriplet = QuadTriplet.split('$')
				del QuadTriplet[-1]
				tmpQuadTriplet.append(QuadTriplet)
				## adding the 
			ScanConvert4TParams.append(tmpQuadTriplet) #adding a line of triplets
	ScanConvert4TParams = np.array(ScanConvert4TParams).astype(float)
print "Verification 4T"
print len(ScanConvert4TParams)
print len(ScanConvert4TParams[0])
print len(ScanConvert4TParams[0][0])
