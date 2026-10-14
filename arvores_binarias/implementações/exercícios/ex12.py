import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node
from collections import deque
from tree import BinaryTree

# Uma árvore própria possui nós com 0 ou 2 filhos

def is_propria(root: Node):

    if root is None:
        return True

    queue = deque([root])

    while queue:

        node = queue.popleft()
        count_nodes = 0

        # if not ((node.left_child and node.right_child) or (not node.left_child and not node.right_child)):
        #     return False

        if node.left_child:
            count_nodes += 1
            queue.append(node.left_child)

        if node.right_child:
            count_nodes += 1
            queue.append(node.right_child)

        if count_nodes == 1:
            return False

    return True

def is_propria_recursive(root: Node) -> bool:

    if root is None:
        return True

    if not ((root.left_child and root.right_child) or (not root.left_child and not root.right_child)):
        return False

    return is_propria_recursive(root.left_child) and is_propria_recursive(root.right_child)



    
            



