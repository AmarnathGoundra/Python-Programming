""" networkx basics """

import networkx as nx

U=nx.Graph()         #undirected Graph
G=nx.DiGraph()       #Directed Graph

print("Nodes")

print(G.nodes())

G.add_nodes_from([i for i in range(5)])
print(G.nodes())

print(list(G.nodes()))

print("Edges")

print(G.edges())

G.add_edge(1,2)
G.add_edge(0,2)
G.add_edge(2,3)
G.add_edge(4,2)
G.add_edge(3,5)
G.add_edge(5,2)
G.add_edge(0,1)
G.add_edge(5,0)

print(G.edges())
print(G.in_edges())
print(G.out_edges())

print(G.in_edges(2))
print(G.out_edges(2))