import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node

def in_tree(root: Node, item) -> bool:

    if root is None:
        return False

    if root.data == item:
        return True

    result_left = in_tree(root.left_child, item)
    result_rigth = in_tree(root.right_child, item)

    return result_left or result_rigth