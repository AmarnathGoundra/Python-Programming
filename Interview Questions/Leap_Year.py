# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:05:16 2022

@author: Amarnath
"""

year = int(input("Enter the year to check for leap year"))

if((year%400==0) or ((year%4==0) and (year%100!=0))):
    print("Leap Year")
else:
    print("Not a leap year")
    
############################################################

if(year%400==0):
    print("Leap Year")
elif(year%100==0):
    print("Not a Leap Year")
elif(year%4==0):
    print("Leap Year")
else:
    print("Not a Leap Year")

##############################################################

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")