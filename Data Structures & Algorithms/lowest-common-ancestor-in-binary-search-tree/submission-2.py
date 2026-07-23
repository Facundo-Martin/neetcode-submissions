# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasNode(self, current: TreeNode, target: TreeNode) -> bool:
        """
        Helper method to check if a target node exists in a given subtree.
        """
        if not current:
            return False
            
        # Return True if it's the current node, or if it's found in the left or right subtrees
        return (
            current == target or 
            self.hasNode(current.left, target) or 
            self.hasNode(current.right, target)
        )
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case
        if not root:
            return None

        # FIX: If the root itself is p or q, then it must be the LCA.
        # This catches cases where one node is the direct ancestor of the other.
        if root == p or root == q:
            return root
            
        # Check if root is the split point (one node is left, one is right)
        if self.hasNode(root.left, p) and self.hasNode(root.right, q):
            return root
            
        if self.hasNode(root.left, q) and self.hasNode(root.right, p):
            return root
            
        # If it's not the split point, the LCA must be entirely in the left OR right subtree
        lcaLeft = self.lowestCommonAncestor(root.left, p, q)
        lcaRight = self.lowestCommonAncestor(root.right, p, q)
        
        return lcaLeft if lcaLeft else lcaRight
        # Inputs
        # root: TreeNode, 2 <= The number of nodes in the tree <= 100, signed int values, all unique
        # p: Tree node, signed int value ofc, guaranteed to exist
        # q: Tree node, signed int value ofc, guaranteed to exist

        # Constraints & Edge cases
        # "all node values are unique", "p != q" 
        # -> No need to check ancestors of all values that match p or q
        # "p and q will both exist in the BST." -> No need to check for if not p or not q
        # binary search tree (BST) -> For each node, ever left node values is < node.val, and every right node value is > node.val

        # Patterns (Algo design)
        # No clue lmao!

        # Outputs
        # LCA (TreeNode): "The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants"
        # -> Guaranteed to exist.