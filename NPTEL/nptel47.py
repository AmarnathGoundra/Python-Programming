""" Data compression 03"""
""" nptel 48 and 49 are best methods """

import numpy

from PIL import Image

im = Image.open("pawanism.jpg")

pixelMap = im.load()

I = numpy.asanyarray(Image.open("pawanism.jpg"))

print(I)

img = Image.new(im.mode, im.size)
pixelNew = img.load()

#print(pixelMap[1,2][1])

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if(pixelMap[i,j][1]>=0 and pixelMap[i,j][1]<=31):
            pixelNew[i,j]=0
        elif(pixelMap[i,j][1]>=32 and pixelMap[i,j][1]<=63):
            pixelNew[i,j]=1
        elif(pixelMap[i,j][1]>=64 and pixelMap[i,j][1]<=95):
            pixelNew[i,j]=2
        elif(pixelMap[i,j][1]>=96 and pixelMap[i,j][1]<=127):
            pixelNew[i,j]=3
        elif(pixelMap[i,j][1]>=128 and pixelMap[i,j][1]<=159):
            pixelNew[i,j]=4
        elif(pixelMap[i,j][1]>=160 and pixelMap[i,j][1]<=191):
            pixelNew[i,j]=5
        elif(pixelMap[i,j][1]>=192 and pixelMap[i,j][1]<=223):
            pixelNew[i,j]=6
        elif(pixelMap[i,j][1]>=224 and pixelMap[i,j][1]<=255):
            pixelNew[i,j]=7
            
"""   if(pixelMap[i,j][0]>=0 and pixelMap[i,j][0]<=31):
                pixelNew[i,j]=0
            elif(pixelMap[i,j][0]>=32 and pixelMap[i,j][0]<=63):
                pixelNew[i,j]=1
            elif(pixelMap[i,j][0]>=64 and pixelMap[i,j][0]<=95):
                pixelNew[i,j]=2
            elif(pixelMap[i,j][0]>=96 and pixelMap[i,j][0]<=127):
                pixelNew[i,j]=3
            elif(pixelMap[i,j][0]>=128 and pixelMap[i,j][0]<=159):
                pixelNew[i,j]=4
            elif(pixelMap[i,j][0]>=160 and pixelMap[i,j][0]<=191):
                pixelNew[i,j]=5
            elif(pixelMap[i,j][0]>=192 and pixelMap[i,j][0]<=223):
                pixelNew[i,j]=6
            elif(pixelMap[i,j][0]>=224 and pixelMap[i,j][0]<=255):
                pixelNew[i,j]=7
"""
            
"""      
            if(pixelMap[i,j][2]>=0 and pixelMap[i,j][2]<=31):
                pixelNew[i,j]=0
            elif(pixelMap[i,j][2]>=32 and pixelMap[i,j][2]<=63):
                pixelNew[i,j]=1
            elif(pixelMap[i,j][2]>=64 and pixelMap[i,j][2]<=95):
                pixelNew[i,j]=2
            elif(pixelMap[i,j][2]>=96 and pixelMap[i,j][2]<=127):
                pixelNew[i,j]=3
            elif(pixelMap[i,j][2]>=128 and pixelMap[i,j][2]<=159):
                pixelNew[i,j]=4
            elif(pixelMap[i,j][2]>=160 and pixelMap[i,j][2]<=191):
                pixelNew[i,j]=5
            elif(pixelMap[i,j][2]>=192 and pixelMap[i,j][2]<=223):
                pixelNew[i,j]=6
            elif(pixelMap[i,j][2]>=224 and pixelMap[i,j][2]<=255):
                pixelNew[i,j]=7
"""
img.save("pawanism_gray.jpg")

J = numpy.asanyarray(Image.open("pawanism_gray.jpg"))

print(J)