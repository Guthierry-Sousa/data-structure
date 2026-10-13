import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node
from tree import BinaryTree
from collections import deque

def count_node(root: Node) -> int:

    if root is None:
        return 0

    return count_node(root.left_child) + count_node(root.right_child) + 1

def count_node2(root: Node):

    count = 0

    queue_nodes = deque([root])

    while len(queue_nodes) > 0:

        node = queue_nodes.popleft()
        count += 1

        if node.left_child:
            queue_nodes.append(node.left_child)


        if node.right_child:
            queue_nodes.append(node.right_child)

    return count

if __name__ == "__main__":

    tree = BinaryTree(Node('a'))
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    b.left_child = c
    b.right_child = d

    tree.root.left_child = b
    tree.root.right_child = e

    print(count_node2(tree.root))