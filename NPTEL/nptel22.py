"""Bubble sorting, linear searching & binary search"""

def bubble(a):
    n=len(a)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

def linear_search(a,x):
    count=0
    f=0
    
    for i in range(len(a)-1):
        count+=1
        if(a[i]==x):
            print("Found at position",i)
            f=1
            break;
    if f==0:
        print("Not found")
    print("Number of iterations are: ",count)
    
def binary_search(a,x):
    fir_pos=0
    last_pos=len(a)-1
    f=0
    count=0
    
    while(fir_pos<=last_pos & f==0):
        count+=1
        mid=(fir_pos+last_pos)//2
        if x==a[mid]:
            f=1
            print("Found at position : ",mid)
            print("Number of iterations are: ",count)
            return
        else:
            if x>a[mid]:
                fir_pos=mid+1
            else:
                last_pos=mid-1
    print("Number not found")
    
a=[1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,1,34,5,6,6,7,88,7,6,5,4,4,3]

print("Bubble sort")
bubble(a)
print("a=",a)

x=int(input("Enter a number to find"))
print("Linear search")
linear_search(a, x)

print("Binary Search")
binary_search(a,x)