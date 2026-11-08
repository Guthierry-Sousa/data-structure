def max_value_tree(root):

    if root is None:
        return float('-inf')

    return max(root.data, root.left, root.right)