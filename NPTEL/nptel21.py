"""Dictionaries"""

a={}
print("Dictionaries")
print(a)

a["Dollar"]=70
print(a)

a["Euro"]=80
print(a)

print("Value of First dictionary",a["Euro"])

print(a.keys())
print(a.values())
print(list(a.keys()))
print(list(a.values()))
print(a.items())

a["Yen"]=50
print(a)

del a["Yen"]
print(a)

e=5
r=e*a["Euro"]
print("Value in Indian rupee",r)