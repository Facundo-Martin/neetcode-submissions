# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # 1. Serialize both trees (same as the previous approach)
        def serialize(node):
            if not node:
                return "#"
            return f"^{node.val}${serialize(node.left)}{serialize(node.right)}"
        
        root_str = serialize(root)
        subRoot_str = serialize(subRoot)
        
        # 2. Use KMP to search for the subRoot string inside the root string
        return self.kmp_search(root_str, subRoot_str)

    def kmp_search(self, s: str, pattern: str) -> bool:
        if not pattern:
            return True
            
        # Step A: Build the LPS (Longest Prefix Suffix) array for the pattern
        lps = [0] * len(pattern)
        prev_lps = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[prev_lps]:
                prev_lps += 1
                lps[i] = prev_lps
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]
                
        # Step B: Perform the search using the LPS array
        i = 0  # pointer for the main string (s)
        j = 0  # pointer for the pattern
        
        while i < len(s):
            if s[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    # The magic of KMP: skip ahead using the LPS array instead of starting over
                    j = lps[j - 1]
                    
            if j == len(pattern):
                return True # We found the entire pattern
                
        return False

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
