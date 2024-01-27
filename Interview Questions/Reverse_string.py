# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:38:21 2022

@author: Amarnath
"""

str1 = input("Enter the string\n")

str2 = ""
for i in str1:
    str2 = i+str2
    
print("Reverse is:",str2)

#########################################

str3 = ""
i = len(str1)-1
while(i>=0):
    str3 = str3+str1[i]
    i = i-1
    
print("Reverse is:",str3)

##########################################

str4 = str1[::-1]
print("Reverse is:",str4)

##########################################

def reverse(str1):
    if(len(str1)==0):
        return str1
    else:
        return reverse(str1[1:])+str1[0]
    
rev = reverse(str1)
print("Reverse is:",rev)