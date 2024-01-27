""" Area calculation """

from PIL import Image
import random
im=Image.open("map.png")
rgb_im=im.convert("RGB")
count_ind=0
count_telangana=0
count=0
while(count<=100000):
    x=random.randint(0,714)
    y=random.randint(0,807)
    z=0
    r,g,b=rgb_im.getpixel((x,y))
    if(r==232):
        count_ind+=1
        count=count+1
    else:
        if(r==245):
            count_telangana+=1
            count+=1
            
area_telangana=(count_telangana/count_ind)*3287263
print(area_telangana)