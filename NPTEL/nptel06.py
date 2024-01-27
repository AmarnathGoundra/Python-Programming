"""list functions using characters"""

#creating a list
shopping=["bread","coffee","sugar","jam","butter","milk"]
print("execution 1: ")
print(shopping)
    
print("execution 2: ")
for i in range(3):
    print(i)
    print(shopping[i])

print("execution 3: ")
shopping.append("curd")
for i in shopping:
    print(i)

print("execution 4: ")
shopping.insert(1,"oil")
print(shopping[1])

print("execution 5: ")
shopping.sort()
print(shopping)

print("execution 6: ")
print(shopping[:2])
print(shopping[:])
print(shopping[2:])
print(shopping[3:6])

print("execution 7: ")
for i in range(len(shopping)):
    print(shopping[i])