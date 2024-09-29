class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
            # If both nodes are None, they are mirrors
            if not t1 and not t2:
                return True
            # If one of the nodes is None, they are not mirrors
            if not t1 or not t2:
                return False
            # Check if the values of the nodes are equal
            if t1.val != t2.val:
                return False
            # Recursively check the subtrees
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        # Check if the tree itself is symmetric
        return isMirror(root, root)

# Example usage:
if __name__ == "__main__":
    # Create a symmetric tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    # Create an asymmetric tree
    asymmetric_root = TreeNode(1)
    asymmetric_root.left = TreeNode(2)
    asymmetric_root.right = TreeNode(2)
    asymmetric_root.left.right = TreeNode(3)
    asymmetric_root.right.right = TreeNode(3)

    sol = Solution()
    print(sol.isSymmetric(root))  # Output: True
    print(sol.isSymmetric(asymmetric_root))  # Output: False

