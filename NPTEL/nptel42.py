""" calculating Area
Area of telangana """

import imageio
#from scipy.misc import imread
from PIL import Image
import numpy as np
import random

img=imageio.imread("map.png")
count_telangana=0
count_ind=0
count=0
while(count<=100000):
    x=random.randint(0,807)
    y=random.randint(0,714)
    z=0
    if(img[x][y][z]==232):
        count_ind+=1
        count=count+1
    else:
        if(img[x][y][z]==245):
            count_telangana+=1
            count+=1
            
area_telangana=(count_telangana/count_ind)*3287263
print(area_telangana)            

"""
telangana = rgb(245,183,142)
India = rgb(232,228,243)

found on online by searching
rgb finding online"""

#Area of telangana == 112077