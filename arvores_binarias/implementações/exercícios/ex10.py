import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import Node
from collections import deque
from tree import BinaryTree

def inv_nivel(root: Node):

    queue = deque([root])
    stack = deque()

    while queue:

        node = queue.popleft()

        if node.left_child:
            queue.append(node.left_child)

        if node.right_child:
            queue.append(node.right_child)

        stack.appendleft(node)

    size_stack = len(stack)

    for _ in range(size_stack):

        print(stack.popleft().data)

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

    inv_nivel(tree.root)