from network_construction import network_construction
import matplotlib.pylab as plt
import networkx as nx
import itertools as it

colors = it.cycle('bgrcmyk')

G = network_construction('twitter', 'links_r_v')
k = 4

cliques = [clique for clique in nx.k_clique_communities(G, k)]
pos = nx.spring_layout(G)
labels = {}
for node in G.node:
    labels[node] = node
nx.draw_networkx_nodes(G, pos, node_color='w', node_size=500)
nx.draw_networkx_edges(G, pos)
clique_num = 0

for clique in cliques:
    current_color = next(colors)
    nx.draw_networkx_nodes(G, pos, nodelist=clique, node_color=current_color, node_size=500)
    print("\nNo." + str(clique_num+1) + " Clique to appear: ", clique)
    print("Current color: " + current_color)
    for i in range(clique_num):
        for node in clique:
            if node in cliques[i]:
                print("The node " + node + " has been in clique No." + str(i+1))
    clique_num += 1

nx.draw_networkx_labels(G, pos, labels)
plt.show()
