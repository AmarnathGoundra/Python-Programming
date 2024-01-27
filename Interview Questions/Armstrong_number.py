# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:53:36 2022

@author: Amarnath
"""

a = int(input("Enter the number to check for Armstrong number"))
temp = a
n = 0
while(temp>0):
    b = temp%10
    n = n + (b*b*b)
    temp = temp//10
if(n==a):
    print("Armstrong number")
else:
    print("Not a Armstrong number")