"""Knowing color pixel from image """

from PIL import Image
im=Image.open("test1.png")
rgb_im=im.convert("RGB")
r,g,b=rgb_im.getpixel((150,1))
print(r,g,b)
r,g,b=rgb_im.getpixel((1,1))
print(r,g,b)

im=Image.open("map.png")
rgb_im=im.convert("RGB")
r,g,b=rgb_im.getpixel((404,357))
print(r,g,b)