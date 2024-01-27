""" binary search using Recursion"""

def binary_search(l,x,start,end):
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
    else:
        mid=(start+end)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            return binary_search(l, x, mid+1, end)
        else:
            return binary_search(l, x, start, mid-1)
    
l=[1,2,3,4,5,6,7,8,9,0,9,8,7,6,6,4,3,2345,667,88,45]
l.sort()
x=int(input("enter a number to search its position:"))
index=binary_search(l,x,0,len(l)-1)
if index==-1:
    print(x,"not found")
else:
    print(x,"is found at",index+1)
