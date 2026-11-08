class Node:

    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self, root : Node = None):
        self.root = root

    def search(self,root:Node=None, key:int=None):

        if root is None:
            return None

        if root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def insert(self, root, key, value):

        if root is None:
            return Node(key, value)

        if key < root.key:
            root.left = self.insert(root.left, key, value)

        if key > root.key:
            root.right = self.insert(root.right, key, value)

        return root

    def delete(self, root, key):

        if root is None:
            return None

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:

            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            sucessor = root.right

            while sucessor.left:
                sucessor = sucessor.left

            root.key = sucessor.key
            root.right = self.delete(root.right, sucessor.key)

        return root


