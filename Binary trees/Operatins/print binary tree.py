#    1     1 : 2,3   printing of binary tree
#   / \    2 : 4,5
#  2   3   4 :  
# / \      5 :
# 4  5     3 :

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def PrintTree(root):                     
    if root == None:                    
        return
    print(root.data)
    PrintTree(root.left)
    PrintTree(root.left)

def PrintTreeDetailed(root):
    if root == None:
        return
    print(root.data)
    if root.left!=None:
        print("L", root.left.data, end=",")
    if root.right!=None:
        print("R", root.right.data, end="")
    print()
    PrintTreeDetailed(root.left)
    PrintTreeDetailed(root.right)



bt1=BinaryTree(1)
bt2=BinaryTree(2)
bt3=BinaryTree(3)
bt1.left=bt2
bt1.right=bt3


PrintTreeDetailed(bt1)