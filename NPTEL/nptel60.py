""" CCollatz Conjecture"""
""" 
even --> n/2
odd --> 3n+1
"""

def checkNum(num):
    iterations=1
    
    while(num!=1):
        if(num%2 ==0):
            num = int(num/2)
            iterations+=1
        else:
            num= (num*3)+1
            iterations+=1
            
    print(num, iterations)
    
checkNum(75)