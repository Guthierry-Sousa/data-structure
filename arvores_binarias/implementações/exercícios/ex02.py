import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node
from collections import deque

def min_value_recursive(root: Node):

    if root is None:
        return float('inf')

    if root.left_child == None and root.right_child == None:
        return root.data

    return min(root.data, min_value_recursive(root.left_child), min_value_recursive(root.right_child))

def min_value_iter(root: Node):

    queue_nodes = deque([root])
    min_value = float('inf')

    while len(queue_nodes) > 1:

        node = queue_nodes.popleft()

        if node.data < min_value:
            min_value = node.data

        if node.left_child:
            queue_nodes.append(node.left_child)

        if node.right_child:
            queue_nodes.append(node.right_child)

    return min_value