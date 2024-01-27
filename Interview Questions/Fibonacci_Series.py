# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:35:56 2022

@author: Amarnath
"""

a = int(input("Enter the range of FIBONACCI SERIES"))
x = 0
y = 1
for i in range(a):
    if(i<=1):
        next = i
    else:
        next = x+y
        x = y
        y = next
    print(next,end="  ")