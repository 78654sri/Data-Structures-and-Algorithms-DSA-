class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodesGreaterThanX(root, X):
    if root is None:
        return 0
    
    count = 0
    if root.val > X:
        count = count +1
    
    count = count +countNodesGreaterThanX(root.left, X)
    count =count +countNodesGreaterThanX(root.right, X)
    
    return count

if __name__ == "__main__":
    # Example usage:
    
    # Sample input 1: [1, 4, 2, 3, -1, -1, -1] and X = 2
    nodes = TreeNode(1)
    nodes.left = TreeNode(4)
    nodes.right = TreeNode(2)
    nodes.left.left = TreeNode(3)
    
    X = 2
    
    # Calculate and print the result
    result = countNodesGreaterThanX(nodes, X)
    print(result)  # Output should be 2 for this example
