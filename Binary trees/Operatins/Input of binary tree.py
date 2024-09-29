class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def PrintTree(root):
    if root is None:
        return
    print(root.data)
    PrintTree(root.left)
    PrintTree(root.right)

def PrintTreeDetailed(root):
    if root is None:
        return
    print(root.data, end=": ")
    if root.left is not None:
        print("L", root.left.data, end=", ")
    if root.right is not None:
        print("R", root.right.data, end="")
    print()
    PrintTreeDetailed(root.left)
    PrintTreeDetailed(root.right)

def takeInput():
    print("Enter root data")
    rootData = int(input())
    
    if rootData == -1:
        return None
    
    root = BinaryTreeNode(rootData)
    root.left = takeInput()
    root.right = takeInput()
    
    return root

root = takeInput()
PrintTreeDetailed(root)
