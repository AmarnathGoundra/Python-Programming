# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 11:45:09 2022

@author: Amarnath
"""

a = int(input("Enter a number to check for prime"))
count = 0
for i in range(2,a//2):
    if(a%i==0):
        count=count+1
if(count==0):
    print("Its a prime number")
else:
    print("Not a prime number")

################################################################
    
a = int(input("Enter the number to print prime numbers"))
print("Prime numbers from 1 to",a,"are:   ")
for i in range(2,a+1):
    count=0
    for j in range(2,i//2+1):
        if(i%j==0):
            count=count+1
    if(count==0):
        print(i)