"""fizbuzz"""

def fizbuzz(r):
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print("fizbuzz")
        elif(i%3==0):
            print("fiz")
        elif(i%5==0):
            print("buzz")
        else:
            print(i)
    return r
fizbuzz(51)