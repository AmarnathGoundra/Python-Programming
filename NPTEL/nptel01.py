"""Calculating discount"""
print("hi, lets make the final bill")
cost=input("enter the cost")
cost=int(cost)
discount=input("enter the discount in percentage")
discount=int(discount)
bill=((100-discount)/100)*cost
print("the final bill is",bill,"only")
print("thank you")