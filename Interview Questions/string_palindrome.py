# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:57:03 2022

@author: Amarnath
"""

def checkpalindrome(st):
    for i in range(0,len(st)//2):
        if st[i] != st[len(st)-1-i]:
            return False
    return True

st = input("Enter a number\n")

if(checkpalindrome(st) == True):
    print("Given is a Palindrome")
else:
    print("Given is not a Palindrome")
    
# Method 2

def checkpali(st):
    rev = st[::-1]
    return "Palindrome" if rev==st else "Not a Palindrome"
    
print(checkpali(st))