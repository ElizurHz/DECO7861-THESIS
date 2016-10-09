from network_construction import network_construction
import community
import matplotlib.pyplot as plt
import networkx as nx

G = network_construction('twitter', 'links_r_v')

partition = community.best_partition(G)
pos = nx.spring_layout(G)
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
labels = {}

for com in set(partition.values()):
    labels.clear()
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    for nodes in partition.keys():
        if partition[nodes] == com:
            labels[nodes] = nodes
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size=500, node_color=colors[com], label=True)
    nx.draw_networkx_labels(G, pos, labels)
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()
