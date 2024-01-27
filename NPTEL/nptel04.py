"""Sum of n numbers"""
a=input("Say a number to find the sum of the number from zero")
a=int(a)
c=0
for i in range(a+1):
    c=c+i
print("sum of",a,"numbers is",c)