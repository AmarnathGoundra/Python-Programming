""" network """

import networkx as nx
import matplotlib.pyplot as plt

#Graph 1

G=nx.Graph()

G.add_node(1)

G.add_node(2)

G.add_node(3)

G.add_edge(1,2)

G.add_edge(3,2)

G.add_edge(1,3)

print(G.edges())

nx.draw(G)
plt.title("Graph 1")
plt.show()

#Graph 2

H=nx.Graph()

l=[1,2,3]

H.add_nodes_from(l)

H.add_edge(1,2)

H.add_edge(3,2)

H.add_edge(1,3)

print(H.edges())

nx.draw(H)
plt.title("Graph 2")
plt.show()

#Graph 3

I=nx.complete_graph(10)
nx.draw(I)
plt.title("Graph complete")
plt.show()

#Graph 4

J=nx.gnp_random_graph(10,0.2)
nx.draw(J)
plt.title("Graph random")
plt.show()