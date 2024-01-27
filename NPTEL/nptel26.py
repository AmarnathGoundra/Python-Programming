""" Game X or O """

import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='x'
p2s='o'

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        r=int(input("Enter row - 1,2,3\n"))
        c=int(input("Enter column - 1,2,3\n"))
        if r>0 and r<4 and c<4 and c>0 and board[r-1][c-1]=='-':
            break
        else:
            print("Please enter a valid input")
    board[r-1][c-1]=symbol
    
def check_row(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol, " WON!!!!")
            return True
    return False

def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol, " WON!!!!")
            return True
    return False

def check_diag(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol," WON!!!!")
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol," WON!!!!")
        return True
    return False
    
def won(symbol):
    return check_row(symbol) or check_col(symbol) or check_diag(symbol)

def play():
    for turn in range(9):
        if turn%2==0:
            print("x turn!!!")
            place(p1s)
            if won(p1s):
                print(numpy.matrix(board))
                break
        else:
            print("o turn!!!")
            place(p2s)
            if won(p2s):
                print(numpy.matrix(board))
                break
    
    print("Draw!!!!")

play()