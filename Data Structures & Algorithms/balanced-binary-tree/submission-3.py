# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # If the tree is balanced, it returns the height. 
        # If unbalanced, it returns -1.
        return self.dfsHeight(root) != -1

    def dfsHeight(self, node: Optional[TreeNode]) -> int:
        # Base case: empty node has a height of 0
        if not node:
            return 0

        # Traverse Left
        leftHeight = self.dfsHeight(node.left)
        # Short-circuit: if left is unbalanced, stop and pass the error up
        if leftHeight == -1:
            return -1

        # Traverse Right
        rightHeight = self.dfsHeight(node.right)
        # Short-circuit: if right is unbalanced, stop and pass the error up
        if rightHeight == -1:
            return -1

        # Current Node Operation: Check balance
        if abs(leftHeight - rightHeight) > 1:
            return -1

        # Return actual height if balanced
        return max(leftHeight, rightHeight) + 1