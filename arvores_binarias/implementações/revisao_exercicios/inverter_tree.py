def inv_tree(root):

    if root is None:
        return None

    aux1 = inv_tree(root.left)
    aux2 = inv_tree(root.right)
    root.left, root.right = aux2, aux1

    return root