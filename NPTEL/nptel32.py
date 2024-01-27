""" image showing """

from PIL import Image

def show_board():
    img = Image.open("Snakes&Ladder.jpg")
    img.show()
    
show_board()