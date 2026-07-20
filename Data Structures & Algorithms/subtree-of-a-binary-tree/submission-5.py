# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case 1: Both trees are empty
        if not root and not subRoot: 
            return True

        # Base Case 2: One of them is empty
        if not root or not subRoot:
            return False

        # Base Case 3: Nodes exist but values don't match
        if root.val != subRoot.val:
            return False

        left_side_match = self.isSameTree(root.left, subRoot.left)
        right_side_match = self.isSameTree(root.right, subRoot.right)

        return left_side_match and right_side_match

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case 1: root is empty and subRoot is not!
        if not root and subRoot:
            return False

        # Base Case 2: subRoot is empty! Counts as subtree btw
        if not subRoot:
            return True

        # Base Case 3: They are exactly the same tree
        if self.isSameTree(root, subRoot):
            return True

        is_left_subtree = self.isSubtree(root.left, subRoot)
        is_right_subtree = self.isSubtree(root.right, subRoot)

        return is_left_subtree or is_right_subtree

        # input:
        # root: Node of the binary tree
        # subroot: Node of the subtree

        # Constraints & Edge cases
        # "subtree of root with the same structure and node values of subRoot" 
        # "tree tree could also be considered as a subtree of itself"
        # -> root.val == subroot.val && root.left == subroot.left && root.right == subroot.right
        # -> For every node!!
        # 1 <= The number of nodes in both trees <= 100 -> No need to deal with empty nodes
        #-100 <= root.val, subRoot.val <= 100 -> self.val is signed int


        # Patterns
        

        # Output:
        # bool: True/False depending on whether tree contains subroot
