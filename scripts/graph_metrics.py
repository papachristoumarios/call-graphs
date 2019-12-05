import networkx as nx
import argparse
import utils
import numpy as np
import multiprocessing
import glob
import os
import tabulate
from pathlib import Path


def get_metrics(filename):
    print('Processing', filename)
    G, system, graph_type = utils.read_graph(filename)

    degrees = np.zeros(len(G))
    for i, v in enumerate(G.nodes()):
        degrees[i] = G.degree(v)

    SCCs = nx.strongly_connected_component_subgraphs(G)
    GCC = max(SCCs, key=len)

    return [
        system,
        graph_type,
        len(G),
        len(G.edges()),
        len(GCC),
        int(degrees.max()),
        int(degrees.min()),
        round(degrees.mean(), 2),
        int(np.median(degrees)),
        nx.algorithms.distance_measures.diameter(GCC)
    ]


if __name__ == '__main__':
    argparser = utils.get_argparser()
    args = argparser.parse_args()
    filenames = []
    i = 0

    results = [['System',
                'Graph Type',
                '# Nodes',
                '# Edges',
                'Size of Giant SCC',
                'Max Degree',
                'Min Degree',
                'Mean Degree',
                'Median Degree',
                'Diameter of GSCC'
            ]]

    for filename in Path(args.r).rglob('**/*graph*.txt'):
        if 'linux' in str(filename):
            continue
        filenames.append(str(filename))
        i += 1

    pool = multiprocessing.Pool(args.w)

    partial_results = pool.map(get_metrics, filenames)
    results.extend(partial_results)

    tabular = tabulate.tabulate(results, tablefmt='latex')

    if args.dry_run:
        print(tabular)
    else:
        with open(args.o, 'w+') as f:
            f.write(tabular)
