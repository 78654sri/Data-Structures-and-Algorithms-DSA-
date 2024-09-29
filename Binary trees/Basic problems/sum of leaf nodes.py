class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumofleafNodes(root):
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return root.data
    else:
        leftSum = sumofleafNodes(root.left) 
        rightSum = sumofleafNodes(root.right)
        return leftSum + rightSum 


# Constructing the binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)


total_sum = sumofleafNodes(root)
print(f"Sum of all nodes: {total_sum}")  # Output should be 21