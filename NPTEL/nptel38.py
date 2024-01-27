""" sorting """

x=[1,4,7,5,3,0,8,6]
print(sorted(x))
print(sorted(x,reverse=True))

print()
x=["s","g","e","a","p","b"]
print(sorted(x))
print(sorted(x,reverse=True))

print()
x="Python"
print(sorted(x))
print(sorted(x,reverse=True))

print()
x={"e":2,"g":3,"a":4,"q":5,"f":7}
print(sorted(x))
print(sorted(x,reverse=True))

print()
L=["aaaaaa","rr","ggg","jjjj"]
print(sorted(L))
print(sorted(L,reverse=True))

print()
L=["aaaaaa","rr","ggg","jjjj"]
print(sorted(L,key=len))