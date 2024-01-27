"""jumbled words game"""

import random

def choose():
    words=['rainbow','computer','laptop','teacher','student','mouse','telugu','hundred','mother','father','college','school','books']
    pick=random.choice(words)
    return pick

def jumble(w):
    jumbled="".join(random.sample(w,len(w)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,"your score is ",p1)
    print(p2n,"your score is ",p2)
    print("Thank you for playing")
    print("Have a nice day")

def play():
    p1name=input("Player 1, enter ypur name!")
    p2name=input("Player 2, enter your name!")
    pp1=0
    pp2=0
    turn=0
    while(1):
        pick_word=choose()
        word=jumble(pick_word)
        print(word)
        if turn%2==0:
            print(p1name,"!, Its your turn..")
            ans=input("enter your answer..")
            if ans==pick_word:
                print("Hurray, it is correct..")
                pp1=pp1+1
                print("your score now --", pp1)
            else:
                print("Better luck next time, i thought ", pick_word)
        else:
            print(p2name,"!, Its your turn..")
            ans=input("enter your answer..")
            if ans==pick_word:
                print("Hurray, it is correct..")
                pp2=pp2+1
                print("your score now --", pp2)
            else:
                print("Better luck next time, i thought ", pick_word)
        turn=turn+1
        c=int(input("Enter 1 to continue/ 0 to exit"))
        if c==0:
            thank(p1name, p2name, pp1, pp2)
            break
play()