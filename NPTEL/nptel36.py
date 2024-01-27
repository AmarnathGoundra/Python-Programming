""" SPIRAL DISPLAY OF DOTS """

import turtle
import random

turtle.bgcolor("black")
ra=turtle.Turtle()

width = 5
height = 7

dot_distance=25

ra.penup()

ra.setpos(-250,250)

list_color=["white","yellow","brown","red","blue","green","orange","pink","violet","grey"]

def spiral(r,c):
    k=0
    l=0
    f=0
    
    """
    k=index of starting row
    l=index of starting column
    """
    while(k<r and l<c):
        
        col=random.randint(0,9)
        ra.color(list_color[col])
        
        if(f==1):
            ra.right(90)
        
        #printing first row from remaining rows
        for i in range(l,c):
            ra.dot()
            ra.forward(dot_distance)
            #print(a[k][i],end=" ")
        
        k=k+1
        f=1
        
        ra.right(90)
        
        col=random.randint(0,9)
        ra.color(list_color[col])
        #printing last column from remaining columns
        for i in range(k,r):
            ra.dot()
            ra.forward(dot_distance)
            #print(a[i][c-1],end=" ")
        
        c=c-1
        
        ra.right(90)
        col=random.randint(0,9)
        ra.color(list_color[col])
        #printing last row from remaining rows
        ##if(k<r):
        for i in range(c-1,l-1,-1):
            ra.dot()
            ra.forward(dot_distance)
            #print(a[r-1][i],end=" ")
        r=r-1
        
        ra.right(90)
        col=random.randint(0,9)
        ra.color(list_color[col])
        #printing first column from remaining columns
        ##if(l<c):
        for i in range(r-1,k-1,-1):
            ra.dot()
            ra.forward(dot_distance)
            #print(a[i][l],end=" ")
        l=l+1
           
#a=[]
#count=1
#n=int(input("Enter the order of square matrix.."))
""" 
for i in range(n):
    l=[]
    for j in range(n):
        l.append(count)
        count=count+1
    a.append(l)
"""
    
spiral(20,20)
turtle.done()