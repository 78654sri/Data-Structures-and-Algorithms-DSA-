class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



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

def NoofNodes(root):
    if root == None:
        return 0
    else:
        leftNode = NoofNodes(root.left) 
        rightNode = NoofNodes(root.right)
        return leftNode + rightNode + 1

root = takeInput()
PrintTreeDetailed(root)
print(NoofNodes(root))