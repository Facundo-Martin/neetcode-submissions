# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: We've reached the bottom (leaves) of both trees simultaneously.
        # If both are null, it means the paths match perfectly up to this point.
        if not p and not q:
            return True
        
        # Base case 2: One tree has a node here, but the other doesn't.
        # This catches structural mismatches (e.g., one tree is deeper than the other).
        if not p or not q:
            return False

        # Base case 3: Both nodes exist. We must verify their data matches.
        # If the values differ, the trees are not identical.
        if p.val != q.val:
            return False

        # Recursive Step: The current nodes match, so we move downwards.
        # We recursively check that BOTH the left branches and right branches match.
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        

        