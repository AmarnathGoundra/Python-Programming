"""Factorial normal method"""

def factorial(n):
    product=1
    for i in range(1,n+1):
        product*=i
    return product

n=int(input("Enter a number to find its factorial.."))
if n<0:
    print("Factorial is not defined for negative numbers....")
else:
    print("Factorial of a number",n,"is",factorial(n))