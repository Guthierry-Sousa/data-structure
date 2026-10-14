import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node
from collections import deque
from tree import BinaryTree

# Uma árvore cheia possui todos os níveis completos, ou seja, todos nós internos possuem dois filhos e os nós externos estão na mesma profundidade

def is_cheia(root: Node):

    if root is None:
            return True

    altura = -1
    queue = deque([root])

    while queue:

        len_q = len(queue)
        altura += 1

        if len_q != 2**altura:
            return False

        for _ in range(len_q):
            node = queue.popleft()

            if node.left_child:
                queue.append(node.left_child)

            if node.right_child:
                 queue.append(node.right_child)

    return True

def altura(root: Node):

    if root is None:
        return -1

    return 1 + max(altura(root.left_child), altura(root.right_child))

def is_cheia_recursive(root: Node):

    if root is None:
        return True

    if not ((root.left_child and root.right_child) or (not root.left_child and not root.right_child)):
        return False

    if altura(root.left_child) != altura(root.right_child):
        return False

    return is_cheia_recursive(root.left_child) and is_cheia_recursive(root.right_child)


            