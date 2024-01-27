"""Eligibility for exam"""
n=input("enter your percentage in exam")
n=int(n)
if(n>=75):
    print("congratulations! you are eligible to write exam \n for free")
if(75>n>=55):
    print("congratulations! you are eligible to write exam \n with the payment of 1500 only")
if(n<55):
    print("Sorry you are not eligible to write the exan")