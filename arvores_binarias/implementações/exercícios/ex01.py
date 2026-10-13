import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node
from collections import deque

def max_value_recursive(root: Node):

    if root is None:
        return float('-inf')

    if root.left_child == None and root.right_child == None:
        return root.data

    return max(root.data, max_value_recursive(root.left_child), max_value_recursive(root.right_child))

def max_value_iter(root: Node):

    max_value = float('-inf')
    queue_tree = deque([root])
    
    while queue_tree:
    
        node = queue_tree.popleft()

        if max_value < node.data:
            max_value = node.data
    
        if node.left_child:
            queue_tree.append(node.left_child)
    
        if node.right_child:
            queue_tree.append(node.right_child)

    return max_value
    