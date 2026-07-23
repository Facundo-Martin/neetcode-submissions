# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        global_max = float('-inf')
        
        def get_max_gain(node):
            # Base case: empty node contributes 0
            if not node:
                return 0
            
            # Recursively get maximum gain from left and right subtrees
            # Maximize gains using Use max(0, ...) to ignore negative paths
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Calculate the maximum path sum that passes through the current node
            current_path_sum = node.val + left_gain + right_gain
        
            # Update the global maximum path sum if current path is better
            nonlocal global_max
            global_max = max(global_max, current_path_sum)
            
            # Return the maximum gain when continuing the path through parent
            # We can only pick one branch (left or right) when going through parent
            return node.val + max(left_gain, right_gain)
            
        get_max_gain(root)
        
        return global_max
        