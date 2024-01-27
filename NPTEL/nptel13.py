"""file handling functions"""

"""  r- read mode
w- writing mode
a- appending mode
r+ - read and write mode

r+  --if we use "write" first and read second -- write mode
if we use "write" second -- appending mode"""

with open("evolution.txt","r+") as myfile:
    myfile.write("I am Amarnath!!!, MGIT")
    print (myfile.read())
myfile.close()

import random

#randint takes including the range values
a=random.randint(1,5)
print(a)

#randrange takes excluding the end range value
b=random.randrange(1,5)
print(b)

#random takes a value between 0 and 1
c=random.random()
print(c)

#randrange(1,x,2) gives odd random numbers
b=random.randrange(1,5,2)
print(b)

#randrange(2,x,2) gives even random numbers
b=random.randrange(2,5,2)
print(b)

#taking random number from list provided
mylist=[11,23,34,45,56,67,78,89,90]
e=random.choice(mylist)
print(e)