# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:43:13 2022

@author: Amarnath
"""

n = int(input("Enter a number to find its factorial"))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("Factorial of the number is: ",fact)

###############################################################

def fact(n):
    if(n<1):
        return 1
    else:
        return n*fact(n-1)

n = int(input("Enter the number to find its factorial"))
print("Factorial of the number is: ",fact(n))

###############################################################

import math
num = int(input("Enter the number to find its factorial"))

print("Factorial of ",num,"is: ",math.factorial(num))