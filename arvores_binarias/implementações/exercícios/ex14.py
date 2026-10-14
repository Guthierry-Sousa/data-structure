import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node
from collections import deque
from tree import BinaryTree

# Uma árvore completa possui todos os níveis completamente preenchidos, exceto possívelmente, o último nível com os nós o mais à esquerda possível.

def is_completa(root: Node):

    if root is None:
            return True
    
    queue = deque([root])
    is_none = False

    while queue:

        node = queue.popleft()

        if node is None:

            is_none = True

        else:

            if is_none:
                return False

            queue.append(node.left_child)
            queue.append(node.right_child)

    return True