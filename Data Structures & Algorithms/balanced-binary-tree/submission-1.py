# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_balance(node):
            # Base Case: Empty spaces have a height of 0
            if not node:
                return 0
                
            # 1. Wait for children to report UP (Bottom-Up)
            left_h = check_balance(node.left)
            right_h = check_balance(node.right)
            
            # 2. Short-circuit: If a child found an imbalance, bubble the error UP
            if left_h == -1 or right_h == -1:
                return -1
                
            # 3. Check current node: If unbalanced, return the error
            if abs(left_h - right_h) > 1:
                return -1
                
            # 4. If everything is fine, pass the current height UP
            return max(left_h, right_h) + 1
            
        # Start the recursion. If it doesn't return -1, the whole tree is balanced.
        return check_balance(root) != -1