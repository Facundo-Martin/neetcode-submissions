# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            # Case 1: Both values are greater, answer is on the right!
            if min(p.val, q.val) > curr.val:
                curr = curr.right
            # Case 2: Both values are smaller, answer is on the left!
            elif max(p.val, q.val) < curr.val:
                curr = curr.left
            # Case 3: Node is the split point! Just return it because it's the ancestor
            else:
                return curr # Guaranteed to exist


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