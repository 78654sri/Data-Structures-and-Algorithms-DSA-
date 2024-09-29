def remove_leaf_nodes(node):
    # If the node is None, return None (base case)
    if node is None:
        return None
    if node.left is None and node.right is None:
        return None
    # Recursively remove leaf nodes from the left and right subtrees
    node.left = remove_leaf_nodes(node.left)
    node.right = remove_leaf_nodes(node.right)

    # If the current node is a leaf, return None to remove it


    # Otherwise, return the current node
    return node
