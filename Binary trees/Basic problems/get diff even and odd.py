class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getLevelDifference(root):
    if not root:
        return 0
    
    # Using a queue for level-order traversal
    queue = [(root, 0)]  # (node, level)
    even_sum, odd_sum = 0, 0
    
    while queue:
        node, level = queue.pop(0)
        
        if level % 2 == 0:
            even_sum += node.val
        else:
            odd_sum += node.val
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return even_sum - odd_sum

# Example usage
# Creating the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)

# Calculate the difference between even and odd level sums
result = getLevelDifference(root)
print("Difference between even and odd level sums:", result)
