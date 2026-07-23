# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: an empty tree has a depth of 0
        if not root:
            return 0
        
        # Recursively find the depth of left and right subtrees
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        
        # The depth of the current node is 1 + the max of its children
        return 1 + max(left_depth, right_depth)