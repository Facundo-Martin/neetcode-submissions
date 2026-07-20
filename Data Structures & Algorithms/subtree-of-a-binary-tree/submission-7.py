# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        # Helper function to serialize the tree into a string
        def serialize(node):
            if not node:
                return "#"
            
            # Use ^ and $ to denote the start and end of a node's value.
            # This prevents false positives (e.g., matching '2' inside '12').
            return f"^{node.val}${serialize(node.left)}{serialize(node.right)}"
        
        # Serialize both trees
        root_str = serialize(root)
        subRoot_str = serialize(subRoot)
        
        # Check if subRoot's string is a substring of root's string
        return subRoot_str in root_str

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
