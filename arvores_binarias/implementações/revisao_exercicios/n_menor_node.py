def n_menor_node(root, k=5):

    count = []

    def in_order(root):

        if root is None: return None

        in_order(root.left)
        count.append(root.data)
        in_order(root.right)

    in_order(root)

    return count[k-1]