from pymongo import *
import networkx as nx
import matplotlib.pyplot as plt
from to_csv import to_csv
import csv

client = MongoClient()
db = client.twitter
collection = db.links

to_csv('link_gugudan_ioi_dia-original', 'twitter', 'links')
G = nx.Graph()

with open('link_gugudan_ioi_dia-filtered' + '.csv', "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow([
        'User Screen Name',
        'Friend Screen Name'
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
                link['friend_screen_name']
            ])

nx.draw(G, with_labels=True)
plt.show()
