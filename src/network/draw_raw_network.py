import matplotlib.pyplot as plt
import networkx as nx
from network_construction import network_construction

G = network_construction('twitter', 'links_r_v')
nx.draw(G, with_labels=True)
plt.show()