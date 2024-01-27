""" network basics """

import networkx as nx
import matplotlib.pyplot as plt

#Graph type - 1 (BARBELL GRAPH)
G=nx.barbell_graph(5,3)
nx.draw(G)
plt.show()

#Graph type - 2 (COMPLETE GRAPH)
H=nx.complete_graph(6)
nx.draw(H)
plt.show()

#Graph type - 3 (Cyclic Graph)
G=nx.cycle_graph(7)
nx.draw(G)
plt.show()

#Graph type - 4 (Ladder)
G=nx.ladder_graph(6)
nx.draw(G)
plt.show()

#Graph type - 5 (path)
G=nx.path_graph(9)
nx.draw(G)
plt.show()

#Graph type - 6 (Star)
G=nx.star_graph(7)
nx.draw(G)
plt.show()

#Graph type - 7 (Wheel)
G=nx.wheel_graph(7)
nx.draw(G)
plt.show()

#Graph type - 8 (random)
G=nx.gnp_random_graph(7,0.5)
nx.draw(G)
plt.show()