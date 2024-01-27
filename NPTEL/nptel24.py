"""Rock Paper Scissor"""

def rock_paper_scissor(num1,bit1,num2,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    print(p1,p2)
    if(player1[p1])==player2[p2]:
        print("Draw")
    elif(player1[p1]=="Rock" and player2[p2]=="Scissor"):
        print("Player 1 wins!!!")
    elif(player1[p1]=="Paper" and player2[p2]=="Rock"):
        print("Player 1 wins!!!")
    elif(player1[p1]=="Scissor" and player2[p2]=="Paper"):
        print("Player 1 wins!!!")
    elif(player1[p1]=="Scissor" and player2[p2]=="Rock"):
        print("Player 2 wins")
    elif(player1[p1]=="Rock" and player2[p2]=="Paper"):
        print("Player 2 wins")
    elif(player1[p1]=="Paper" and player2[p2]=="Scissor"):
        print("Player 2 wins")
    
player1={0:"Rock",1:"Paper",2:"Scissor"}
player2={0:"Paper",1:"Rock",2:"Scissor"}

while(1):
    num1=input("Player 1 enter your number..")
    bit1=int(input("Enter the secret bit position"))
    num2=input("Player 2 enter your number..")
    bit2=int(input("Enter the secret bit position"))
    rock_paper_scissor(num1,bit1,num2,bit2)
    ch=input("Do you want to continue? (Y/N)")
    if ch=="N" or ch=="n":
        break