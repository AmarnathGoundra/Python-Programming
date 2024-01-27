"""Matrix"""

def magic_square(n):
    magicSquare = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append("*")
        magicSquare.append(l)
        
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()
magic_square(5)

# magic = [[0 for i in range(3)] for j in range(3)]