import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random as rd

from node import Node

def build_tree(qtd_nodes: int):

    values = rd.sample(range(1,qtd_nodes+1), k=qtd_nodes)

    nodes = [Node(v) for v in values]

    for i in range(qtd_nodes):

        idx_left = 2*i + 1
        idx_right = 2*i + 2

        if idx_left < qtd_nodes:
            nodes[i].left_child = nodes[idx_left]

        if idx_right < qtd_nodes:
            nodes[i].right_child = nodes[idx_right]

    root = nodes[0]

    return root
