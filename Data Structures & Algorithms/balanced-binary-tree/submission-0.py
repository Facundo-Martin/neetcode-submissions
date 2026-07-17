# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 1. BOTTOM-UP HELPER: Calculates height
    def get_height(self, node):
        if not node:
            return 0
        return max(self.get_height(node.left), self.get_height(node.right)) + 1

    # 2. TOP-DOWN MAIN FUNCTION: Checks balance
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        # Top-Down action: calculate heights for the CURRENT node
        left_h = self.get_height(root.left)
        right_h = self.get_height(root.right)
        
        if abs(left_h - right_h) > 1:
            return False
            
        # Move down to children and repeat the whole process
        return self.isBalanced(root.left) and self.isBalanced(root.right)