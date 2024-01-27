""" Snakes & Ladder """

import random

from PIL import Image

end=100

def show_board():
    img = Image.open("Snakes&Ladder.jpg")
    img.show()

def check_ladder(points):
    if points==8:
        print("Ladder")
        return 26
    elif points==21:
        print("Ladder")
        return 82
    elif points==43:
        print("Ladder")
        return 77
    elif points==50:
        print("Ladder")
        return 91
    elif points==54:
        print("Ladder")
        return 93
    elif points==62:
        print("Ladder")
        return 96
    elif points==66:
        print("Ladder")
        return 87
    elif points==80:
        print("Ladder")
        return 100
    else:
        return points
    
def check_snake(points):
    if points==44:
        print("Snake")
        return 22
    elif points==46:
        print("Snake")
        return 5
    elif points==48:
        print("Snake")
        return 9
    elif points==52:
        print("Snake")
        return 11
    elif points==55:
        print("Snake")
        return 7
    elif points==59:
        print("Snake")
        return 17
    elif points==64:
        print("Snake")
        return 36
    elif points==69:
        print("Snake")
        return 33
    elif points==73:
        print("Snake")
        return 1
    elif points==92:
        print("Snake")
        return 51
    elif points==95:
        print("Snake")
        return 24
    elif points==98:
        print("Snake")
        return 28
    else:
        return points

def reached_end(points):
    if points==end:
        return True
    else:
        return False

def play():
    p1n=input("Player 1, enter your name")
    p2n=input("Player 2, enter your name")
    pp1=0
    pp2=0
    
    turn=0
    
    while(1):
        if turn%2==0:
            print(p1n,", yors turn!!")
            c=input("Press 1 to continue or 0  to quit")
            if c==0:
                print(p1n, "scored ",pp1)
                print(p2n, "scored ",pp2)
                print("Thanks for playing")
                break
            dice=random.randint(1,6)
            print("Dice Showed",dice)
            pp1+=dice
            
            pp1=check_ladder(pp1)
            
            pp1=check_snake(pp1)
            
            if pp1>end:
                pp1=end
            
            print(p1n, "Your score:",pp1)
            
            if reached_end(pp1):
                print(p1n," WON!!!")
                break
            
        else:
            print(p2n,", yors turn!!")
            c=input("Press 1 to continue or 0  to quit")
            if c==0:
                print(p1n, "scored ",pp1)
                print(p2n, "scored ",pp2)
                print("Thanks for playing")
                break
            dice=random.randint(1,6)
            print("Dice Showed",dice)
            pp2+=dice
            
            pp2=check_ladder(pp2)
                    
            pp2=check_snake(pp2)
                    
            if pp2>end:
                pp2=end
                    
            print(p2n, "Your score:",pp2)
                    
            if reached_end(pp2):
                print(p2n," WON!!!")
                break
        turn=turn+1
    
show_board()
play()