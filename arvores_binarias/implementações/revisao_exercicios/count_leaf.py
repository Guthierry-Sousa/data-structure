def count_leaf(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaf(root.left) + count_leaf(root.right)