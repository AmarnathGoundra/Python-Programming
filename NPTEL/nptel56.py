""" Page rank working in Google in selecting Websites """
""" it is moment of path from random node to directed node and 
increasing their repetition and so on
in selection of website """

import networkx as nx
import random
import matplotlib.pyplot as plt
import operator

G=nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G, with_labels=True)
plt.show()

#Taking random source
x=random.choice([i for i in range(G.number_of_nodes())])
dict_counter={}

for i in range(G.number_of_nodes()):
    dict_counter[i]=0

dict_counter[x]+=1

for i in range(10000000):
    list_n=list(G.neighbors(x))
    if(len(list_n)==0):
        x=random.choice([i for i in range(G.number_of_nodes())])
        dict_counter[x]+=1
    else:
        x=random.choice(list_n)
        dict_counter[x]+=1

#page rank gives probability of views
p=nx.pagerank(G)

#print(p)
#print(dict_counter)

sorted_p=sorted(p.items(),key=operator.itemgetter(1))
sorted_dict=sorted(dict_counter.items(),key=operator.itemgetter(1))
#to get same order in sorted_p & sorted_dict ==> we increase iterations in for loop
print(sorted_p)
print(sorted_dict)