# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:06:50 2022

@author: Amarnath
"""

a = int(input("Enter number one "))
b = int(input("Enter number two "))

i = 1
while(i<=a and i<=b):
    if(a%i==0 and b%i==0):
        hcff = i
    i = i + 1
print("HCF is: ",hcff)

#########################################################

x = a
y = b

while(y!=0):
    temp = y
    y = x%y
    x = temp
print("HCF is: ",temp)

##########################################################

x = a
y = b

z = min(x,y)

if(min==0):
    print("HCF is: ",max(x,y))
else:
    while(y!=0):
        if(x>y):
            x=x-y
        else:
            y=y-x
    print("HCF is: ",x)
    
###########################################################

def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b, a%b)

print("HCF of {0} and {1} is {2}".format(a, b, hcf(a,b)))