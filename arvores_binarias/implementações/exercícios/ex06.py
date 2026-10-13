import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node
from tree import BinaryTree
from collections import deque

def altura_da_arvore(root: Node):

    if root is None:
        return -1

    altura_left = altura_da_arvore(root.left_child) # altura da subárvore esquerda
    altura_rigth = altura_da_arvore(root.right_child) # altura da subárvore direita

    return 1 + max(altura_rigth, altura_left)

def altura_da_arvore2(root: Node):

    altura = -1
    queue = deque([root])

    while queue:

        altura += 1
        qtd_node = len(queue)

        for i in range(qtd_node):
            node = queue.popleft()

            if node.left_child:
                queue.append(node.left_child)

            if node.right_child:
                queue.append(node.right_child)

    return altura

    