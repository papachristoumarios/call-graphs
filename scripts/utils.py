import networkx as nx
import numpy as np
import argparse
import os
from multiprocessing import cpu_count

def read_graph(filename):
    dirname, graph_type = os.path.split(filename)
    graph_type = graph_type.strip('_all').strip('*.txt')
    _, system = os.path.split(dirname)

    G = nx.DiGraph()
    with open(filename) as f:
        lines = f.read().splitlines()

    for line in lines:
        u, v = line.split()
        G.add_edge(u, v)

    return G, system, graph_type

def get_argparser():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-r', help='Root directory', default='..')
    argparser.add_argument('-w', help='Number of workers', default=cpu_count()-1)
    argparser.add_argument('-o', help='Output file', default='../results/graph_metrics.tex')
    argparser.add_argument('--dry-run', action='store_true')
    return argparser
