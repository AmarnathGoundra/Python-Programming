""" CYPHERS """

import string
dict={}
data=""
fileo=open("data_encoded.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-10]
print(dict)
with open("data_decoded.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("\nEnd of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        fileo.write(data)
        print(data,end="")
fileo.close()