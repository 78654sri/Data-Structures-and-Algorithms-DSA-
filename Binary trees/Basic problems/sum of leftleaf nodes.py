class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root):
    def isLeaf(node):
        return node and not node.left and not node.right
    
    if not root:
        return 0
    
    left_sum = 0
    if root.left:
        if isLeaf(root.left):
            left_sum += root.left.val
        else:
            left_sum += sumOfLeftLeaves(root.left)
    
    left_sum += sumOfLeftLeaves(root.right)
    
    return left_sum

# Example usage
if __name__ == "__main__":
    # Construct the binary tree from the example
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    # Calculate and print the sum of left leaves
    result = sumOfLeftLeaves(root)
    print(f"Sum of left leaves in the binary tree: {result}")
