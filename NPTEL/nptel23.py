"""Lucky draw"""

import random
doors=[0]*3
goat_doors=[]
swap=0
dont_swap=0
j=0
while j<3:
    x=random.randint(0,2)
    for i in range(0,3):
        if i==x:
            doors[x]="BMW"
        else:
            doors[i]="Goat"
            goat_doors.append(i)
    print("door 0 : ***")
    print("door 1 : ***")
    print("door 2 : ***")
    print("Try your luck to win BMW car!!!!!")
    choice=int(input("Enter your choice"))
    door_open=random.choice(goat_doors)
    while door_open==choice:
        door_open=random.choice(goat_doors)
    print("door",door_open,": Goat")
    ch=input("Do you want to swap? (Y/N)")
    if ch=="y" or ch=="Y":
        print(doors)
        if doors[choice]=="Goat":
            print("You win.. Congratulations!!!")
            swap+=1
        else:
            print("You lost,, Better luck next time...")
    else:
        print(doors)
        if doors[choice]=="BMW":
            print("You win.. Congratulations!!!")
            dont_swap+=1
        else:
            print("You lost,, Better luck next time...")
    j+=1
    doors=[0]*3
    goat_doors=[]
    
print("Swap wins ",swap," times")
print("Dont swap wins ",dont_swap," times")