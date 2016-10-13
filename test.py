import matplotlib.pyplot as plt

import networkx as nx

G=nx.Graph()
nodes = [0,1,2,3,4,5,6,7]
edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4)]
G.add_nodes_from(nodes)
G.add_edges_from(edges)
G.node[1] = 'test'
G[2][3]['value'] = 100
G[0][1] = 9


def draw(graph: object, nodes: list, edges: list):
    pos=nx.circular_layout(G)

    nx.draw_networkx_nodes(G,pos, node_size=2000, node_color='w')
    nx.draw_networkx_edges(G,pos)

    node_labels = {}
    for node in G.nodes():
        node_labels[node] = node
    nx.draw_networkx_labels(G, pos, node_labels)

    edge_labels = {}
    for edge in G.edges():
        edge_labels[edge] = G[edge[0]][edge[1]]
    nx.draw_networkx_edge_labels(G, pos, edge_labels)


    plt.axis('off')
    #plt.savefig("labels_and_colors.png") # save as png
    plt.show() # display

draw(G, nodes, edges)
