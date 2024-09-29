class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def updateTreeInOrder(root, depth):
    if root is None:
        return
    

    updateTreeInOrder(root.left, depth + 1)
    

    root.data = depth
    print(root.data, end=" ")
    

    updateTreeInOrder(root.right, depth + 1)



# Creating a sample binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder traversal before updating depth:")
# Inorder traversal before updating depth
# Expected output: 4 2 5 1 3
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data, end=" ")
        inorderTraversal(root.right)

inorderTraversal(root)
print()

print("Inorder traversal after updating depth:")
# Update tree with depth and print inorder
# Expected output: 2 1 3 1 2
updateTreeInOrder(root, 1)
print()





