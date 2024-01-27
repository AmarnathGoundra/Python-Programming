""" Drawing a graph from nodes given in fille """

import networkx as nx
import matplotlib.pyplot  as plt

G=nx.read_edgelist(r"nodes.txt", create_using=nx.DiGraph(),nodetype=int)

nx.draw(G,with_labels=True)
plt.show()
