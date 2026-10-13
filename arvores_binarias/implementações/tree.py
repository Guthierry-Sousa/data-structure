from node import Node
from collections import deque

class BinaryTree:

    def __init__(self, root : Node = None):
        self.root = root

    def in_order(self, node: Node): # Varredura em ordem

        current = node

        if current is None:
            return

        self.in_order(current.left_child)
        print(current.data)
        self.in_order(current.right_child)

    def pre_order(self, node: Node): # Varredura pré-ordem

        current = node

        if current is None:
            return

        print(current.data)
        self.pre_order(current.left_child)
        self.pre_order(current.right_child)

    def post_order(self, node: Node): # Varredura pós-ordem

        current = node

        if current is None:
            return

        self.pos_order(current.left_child)
        self.pos_order(current.right_child)
        print(current.data)

    def level_order(self, node: Node): # Varredura por nível

        list_of_nodes = set()

        queue_tree = deque([node])

        while queue_tree:

            node = queue_tree.popleft()
            list_of_nodes.add(node.data)

            if node.left_child:
                queue_tree.append(node.left_child)

            if node.right_child:
                queue_tree.append(node.right_child)

        return list_of_nodes
        
    