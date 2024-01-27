"""Factorial recursion method"""

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a number to find its factorial.."))
if n<0:
    print("Factorial is not defined for negative numbers....")
else:
    print("Factorial of a number",n,"is",factorial(n))
    