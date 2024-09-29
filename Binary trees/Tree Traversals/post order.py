
#Post-order Traversal: Left, Right, Root
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def postorder(root):
            if root == None:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res

# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.postorderTraversal(root))  # Output should be [3, 2, 1]
