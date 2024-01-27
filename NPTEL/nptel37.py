""" Reverse of a image """

from PIL import Image

img=Image.open("reverse.png")

transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)

transposed_img.save("rev_correct.png")

print("Done Flipping")