class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNodesMultiplesOfM(root, M):
    if root is None:
        return 0
    
    sum_value = 0
    
    # Check if current node value is multiple of M
    if root.val % M == 0:
        sum_value += root.val
    
    # Recursively process left subtree
    sum_value += sumNodesMultiplesOfM(root.left, M)
    
    # Recursively process right subtree
    sum_value += sumNodesMultiplesOfM(root.right, M)
    
    return sum_value

# Example usage
if __name__ == "__main__":
    # Construct the binary tree from the example
    root = TreeNode(10)
    root.left = TreeNode(8)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(12)
    
    M = 5
    
    # Calculate and print the result
    result = sumNodesMultiplesOfM(root, M)