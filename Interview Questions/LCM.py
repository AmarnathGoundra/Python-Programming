# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:16:15 2022

@author: Amarnath
"""

a = int(input("Enter first number"))
b = int(input("Enter second number"))
print()

if(a>b):
    maxi = a
else:
    maxi = b
    
while(True):
    if(maxi%a==0 and maxi%b==0):
        print("LCM of {0} and {1} is: {2}".format(a, b, maxi))
        break
    maxi += 1
print()

########################### METHOD 2 ##############################

x = a
y = b

while(b!=0):
    temp = b
    b = a%b
    a = temp
    
print("HCF of {0} and {1} is {2}".format(x, y, a))

print("LCM is: ",(x*y)/a)
print()

#################### METHOD 3 ###################################

def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b, a%b)

a = x
b = y
    
print("HCF of {0} and {1} is {2}".format(a, b, hcf(a,b)))

print("LCM is: ",(a*b)/hcf(a,b))
