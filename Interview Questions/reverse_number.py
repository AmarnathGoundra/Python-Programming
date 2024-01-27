# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:29:22 2022

@author: Amarnath
"""

n = int(input("Enter the number"))
rev = 0
while(n>0):
    rem = n%10
    rev = rev*10 + rem
    n = n//10
print("Reverse of number is: ",rev)

########################################################

n = int(input("Enter the number"))
rev = 0
def reverse(n):
    global rev
    while(n>0):
        rem = n%10
        rev = rev*10 + rem
        n = n//10
    return rev
print("Reverse of number is: ",reverse(n))
