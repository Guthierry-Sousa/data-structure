import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node
from tree import BinaryTree
from collections import deque

def profundidade(root: Node):

    if root is None:
        return -1

    prof_left = profundidade(root.left_child)
    prof_right = profundidade(root.right_child)

    return 1 + max(prof_left, prof_right)

def profundidade2(root: Node):

    prof = -1
    queue = deque([root])

    while queue:

        prof += 1
        qtd_node = len(queue)

        for i in range(qtd_node):
            node = queue.popleft()

            if node.left_child:
                queue.append(node.left_child)

            if node.right_child:
                queue.append(node.right_child)

    return prof