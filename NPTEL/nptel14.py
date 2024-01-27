"""theory of evolution"""

import random

def evolve(x):
    ind=random.randint(0,len(x)-1)
    p=random.randint(1,5)
    print(p)
    if p==1:
        if x[ind]==1:
            x[ind]=0
        else:
            x[ind]=1

with open("evolution.txt") as myfile:
    x=myfile.read()
    print(x)
    x=list(x)
for i in range(1,10):
    evolve(x)
x=int("".join(map(str,x)))
print(x)
