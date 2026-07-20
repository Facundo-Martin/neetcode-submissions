# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: 
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False

        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case 1: subRoot is empty -> always a subtree
        if not subRoot:
            return True
            
        # Base Case 2: root is empty but subRoot is not -> cannot be a subtree
        if not root:
            return False

        # If they are the same tree, we found our match!
        if self.isSameTree(root, subRoot):
            return True

        # Check if it exists in EITHER the left or right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

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
