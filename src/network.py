from pymongo import *
import networkx as nx
import matplotlib.pyplot as plt
from to_csv import to_csv
import csv
import community

client = MongoClient()
db = client.twitter
collection = db.links

to_csv('link_gugudan_ioi_dia-original', 'twitter', 'links')
G = nx.Graph()

with open('link_gugudan_ioi_dia-filtered' + '.csv', "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow([
        'Source',
        'Target',
        'Type'
    ])
    for link in collection.find(no_cursor_timeout=True):
        if (link['user_screen_name'] in G.nodes() and link['friend_screen_name'] in G.nodes()
            and (link['user_screen_name'], link['friend_screen_name'])in G.edges()):
            print("Link between " + link['user_screen_name']
                  + " and " + link['friend_screen_name'] + " has already existed.")
        else:
            G.add_node(link['user_screen_name'])
            G.add_node(link['friend_screen_name'])
            G.add_edge(link['user_screen_name'], link['friend_screen_name'])
            print ("Edge between " + link['user_screen_name'] + " and "
                   + link['friend_screen_name'] + " has been added")
            csv_writer.writerow([
                link['user_screen_name'],
                link['friend_screen_name'],
                'undirected'
            ])

partition = community.best_partition(G)
size = float(len(set(partition.values())))
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
# nx.draw(G, with_labels=True)
plt.show()
