from collections import deque
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root is None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root is None:
        return
    print(root.data, end=": ")
    if root.left is not None:
        print(f"L {root.left.data}", end=", ")
    if root.right is not None:
        print(f"R {root.right.data}", end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def takeInputLevelWise():
    print("Enter root data")
    rootData = int(input())
    
    if rootData == -1:
        return None
    
    root = BinaryTreeNode(rootData)
    queue = deque([root])
    
    while queue:
        currentNode = queue.popleft()
        
        print(f"Enter left child of {currentNode.data}")
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            currentNode.left = leftChild
            queue.append(leftChild)
        
        print(f"Enter right child of {currentNode.data}")
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            currentNode.right = rightChild
            queue.append(rightChild)
    
    return root

root = takeInputLevelWise()
printTreeDetailed(root)

