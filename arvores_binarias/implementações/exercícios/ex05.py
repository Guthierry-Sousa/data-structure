import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node
from tree import BinaryTree
from collections import deque

def level_max_value(root: Node, nivel: int = 1, dict_sum_nivel: dict = None) -> int:

    if dict_sum_nivel is None:
        dict_sum_nivel = {}

    if root is None:
        return None

    if dict_sum_nivel.get(nivel) is None:

        dict_sum_nivel[nivel] = root.data

    else:

        dict_sum_nivel[nivel] += root.data

    level_max_value(root.left_child, nivel+1, dict_sum_nivel)
    level_max_value(root.right_child, nivel+1, dict_sum_nivel)

    return max(dict_sum_nivel, key=dict_sum_nivel.get)

def level_max_value2(root: Node):

    nivel_final = None
    nivel = 0
    maior_soma_nivel = float('-inf')
    queue = deque([root])

    while queue:

        qtd_nodes = len(queue) # Saber quantos nós existe em determinado nível
        soma_nivel = 0
        nivel += 1

        for _ in range(qtd_nodes): # Processa todo nível

            node = queue.popleft()
            soma_nivel += node.data

            if node.left_child:
                queue.append(node.left_child)

            if node.right_child:
                queue.append(node.right_child)

        if soma_nivel > maior_soma_nivel:
            maior_soma_nivel = soma_nivel
            nivel_final = nivel

    return nivel_final

if __name__ == "__main__":

    tree = BinaryTree(Node(1))
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    b.left_child = c
    b.right_child = d

    tree.root.left_child = b
    tree.root.right_child = e

    print(level_max_value(tree.root))
    print(level_max_value2(tree.root))
