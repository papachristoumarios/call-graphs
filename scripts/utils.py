import networkx as nx
import numpy as np

def read_graph(filename):

    G = nx.DiGraph()
    with open(filename) as f:
        lines = f.read().splitlines()

    for line in lines:
        u, v = line.split()
        G.add_edge(u, v)

    return G
