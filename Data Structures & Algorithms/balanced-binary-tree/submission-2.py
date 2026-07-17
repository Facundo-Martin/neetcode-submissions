# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # The helper returns a tuple: (is_balanced, height)
        # We extract index [0] to get the final boolean answer
        return self.dfs(root)[0]

    def dfs(self, node: Optional[TreeNode]) -> Tuple[bool, int]:
        # Base case: an empty tree is balanced (True) and has a height of 0
        if not node:
            return (True, 0)
        
        # Traverse both Left and Right (No short-circuiting)
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        # Current Node Operation:
        # It is balanced if: left is balanced AND right is balanced AND height diff <= 1
        is_current_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        
        # Calculate current height
        current_height = 1 + max(left[1], right[1])
        
        # Pass the state pair up to the parent
        return (is_current_balanced, current_height)