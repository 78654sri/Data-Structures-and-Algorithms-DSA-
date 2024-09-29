from collections import deque

class Solution:
    def levelOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            res.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res

# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.levelOrderTraversal(root))  # Output should be [1, 2, 3]
