"""
needs:

    pygraphviz
    pydotplus
    networkx
    matplotlib
"""
import networkx as nx
import matplotlib.pyplot as plot

G=nx.MultiDiGraph()
nodes = ['a','b','c','d','e','f','g']
edges = [('a','b'),('b','c'),('b','d'),('a','e'),('e','f'),('e','g')]

G.add_nodes_from(nodes)
G.add_edges_from(edges)


def draw(graph: object, nodes: list, edges: list,
         root=nodes[0], output="", layout='circo',
         node_size=1000, node_color='w', node_labels=True,
         edge_width=1.0, edge_color='k', edge_labels=True, edge_arrows=False):

    # graphviz prog options:
    # 'dot' = good for trees
    # 'circo' = seems good for others
    # 'neato' = looks good when circo crosses edges
    layout_map = {'tree': 'dot', 'neat': 'neato', 'neat2': 'circo'}
    pos = nx.nx_pydot.graphviz_layout(graph, root=root, prog=layout_map[layout])

    nx.draw_networkx_nodes(graph,pos, node_size=node_size,
                           node_color=node_color)
    nx.draw_networkx_edges(graph, pos, width=edge_width, edge_color=edge_color,
                           arrows=edge_arrows)

    if node_labels:
        node_labels = {}
        for node in graph.nodes():
            node_labels[node] = node
        nx.draw_networkx_labels(graph, pos, node_labels)

    if edge_labels:
        edge_labels = {}
        for edge in graph.edges():
            edge_labels[edge] = G[edge[0]][edge[1]]
        nx.draw_networkx_edge_labels(graph, pos, edge_labels)

    plot.axis('off')
    if output != "":
        plot.savefig(output)
    plot.show()

draw(G, nodes, edges, layout='neat2', output="test.png", edge_arrows=True)
