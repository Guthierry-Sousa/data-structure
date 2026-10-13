import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node

def number_nodes(root: Node):

    if root is None:
        return 0

    return 1 + number_nodes(root.left_child) + number_nodes(root.right_child)