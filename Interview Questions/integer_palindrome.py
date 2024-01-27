# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:20:07 2022

@author: Amarnath
"""

def reverse(b):
    x = 0
    while(b != 0):
        x = (x*10)+(b%10)
        b = b//10
    return x

a = int(input("Enter a number"))
r = reverse(a)

if (r==a):
    print("Given number is palindrome")
else:
    print("Give number is not a palindrome")
    
    
# Method 2

def checkpalindrome(c):
    c = str(c)
    rev = c[::-1]
    return "Palindrome" if rev==c else "Not a Palindrome"

print(checkpalindrome(a))