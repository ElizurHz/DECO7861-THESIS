from pymongo import *
import networkx as nx
import matplotlib.pyplot as plt

client = MongoClient()
db = client.twitter
collection = db.links

G = nx.Graph()

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

nx.draw(G, with_labels=True)
plt.draw()
plt.show()