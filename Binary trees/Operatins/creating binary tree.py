class BinaryTreeNode:
    def __init__(self,data):#right now we dont have any child so left and right should be None
        self.data=data
        self.left=None
        self.right=None
bt1= BinaryTreeNode(1)
bt2 =BinaryTreeNode(2)
bt3 =BinaryTreeNode(4)     
bt1.left=bt2
bt1.right=bt3