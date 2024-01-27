""" converting image to gray image 01"""

import numpy

from PIL import Image

im = Image.open("netaji.jpg").convert("L")

pixelMap = im.load()

im.save("Netaji_gray.jpg")


#rgb values of real image 
I = numpy.asanyarray(Image.open("netaji.jpg"))

print(I)