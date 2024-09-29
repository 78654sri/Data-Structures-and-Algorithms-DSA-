from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_duplicate_values(root):
    if root is None:
        return False
    
    seen_values = set()
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node.value in seen_values:
            return True
        seen_values.add(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return False

# Example usage:
# Create a binary tree with duplicates
#        1
#      /   \
#     2     3
#    / \   / \
#   4   2 6   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)  # Duplicate value
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Check for duplicates
print(find_duplicate_values(root))   # Output: True






from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_duplicate_values(root):
    if root is None:
        return False
    
    seen_values = set()
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node.value in seen_values:
            return True
        seen_values.add(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return False

# Example usage:
# Create a binary tree with duplicates
#        1
#      /   \
#     2     3
#    / \   / \
#   4   2 6   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)  # Duplicate value
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Check for duplicates
print(find_duplicate_values(root))   # Output: True
