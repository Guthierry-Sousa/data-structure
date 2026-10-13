import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node
from tree import BinaryTree
from collections import deque

def sum_nodes(root: Node) -> int:

    if root is None:
        return 0

    return sum_nodes(root.left_child) + sum_nodes(root.right_child) + root.data

def sum_nodes2(root: Node):

    if root is None:
        return 0

    somatorio = 0

    queue_nodes = deque([root])

    while len(queue_nodes) > 0:

        node = queue_nodes.popleft()
        somatorio += node.data

        if node.left_child:
            queue_nodes.append(node.left_child)


        if node.right_child:
            queue_nodes.append(node.right_child)

    return somatorio

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

    print(sum_nodes2(tree.root))

