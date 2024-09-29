class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def large(root):
    if root is None:
        return 0
    else:
        left = large(root.left) 
        right = large(root.right)
        largest = max(left, right , root.data)
        return largest

# Constructing the binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)


total_sum = large(root)
print(f"largest node: {total_sum}")  # Output should be 21
