""" Flames """

import string

def remove_matching_letter(l1,l2):
                
    for i in l1[:]:
        if i in l2:
            l1.remove(i)
            l2.remove(i)
                
    l=l1+["*"]+l2
    return [l, True]

p1=input("Enter Person 1 name: ")
p1=p1.lower()
p1=p1.replace(" ","")

p2=input("Enter Person 2 name: ")
p2=p2.lower()
p2=p2.replace(" ","")

l1=list(p1)
l2=list(p2)

proceed=True
while proceed:
    ret_list=remove_matching_letter(l1,l2)
    con_list=ret_list[0]
#    print(ret_list)
#    print(con_list)
    proceed=con_list[1]
#    print(proceed)
    star_index=con_list.index('*')
    l1=con_list[:star_index]
    l2=con_list[star_index+1:]
    break

#print(l1,l2)

count=len(l1)+len(l2)
result=["Friends","Love","Affection","Marriage","Enemy","Sister"]

while len(result)>1:
    split_index=(count%len(result))-1
    if split_index>=0:
        right=result[split_index+1:]
        left=result[:split_index]
        result=right+left
    else:
        result=result[:len(result)-1]
        
print(result[0])
        