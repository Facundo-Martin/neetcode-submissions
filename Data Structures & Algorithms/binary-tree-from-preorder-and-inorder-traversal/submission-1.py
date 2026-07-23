# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if there are no elements to process, the subtree is empty
        if not preorder or not inorder:
            return None

        # 1. The first element of preorder is always the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 2. Find the index of the root in inorder to split left and right subtrees
        mid = inorder.index(root_val)

        # 3. Recursively build the left and right subtrees
        # Left preorder: skip the root (index 1) and take 'mid' amount of elements
        # Left inorder: everything strictly before mid
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # Right preorder: everything after the left subtree's elements
        # Right inorder: everything strictly after mid
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        # Invariants (inorder):
            # If there's only 1 int before root, then there's only 1 level on the left side
                # -> [root, left_node, null, null]
            # If there are 2 ints, then we have 2 levels on it
                # -> [root, left_node, left_node_2, null] OR
                # -> [root, left_node, null, left_right_node]
            # If there are 3 ints, then we could have. 2 or 3 levels!:
                # -> [root, left_node, left_node_2, left_right_node1] OR
                # -> [root, left_node, left_node_2, null, left_node_3, null] OR
                # -> [root, left_node, null, left_right_node1_null_ left_right_node1]
        
        # ========================================
        # PROBLEM SCOPING & ALGO DESIGN
        # ========================================

        # Inputs
            # preorder: preorder traversal of a binary tree
            # inorder: preorder traversal of a binary tree
                # 1D arrays, same size and unique values, signed integers

        # Algo design:
            # Edge cases: length == 1 -> return root?
            # Invariants:
                # preorder traversal goes root -> left -> right
                # inorder traversal goes left -> root -> right
                # Outputs format is in levels, left to right -> BFS
            # Short circuit: None, need to traverse entire tree
            # State: TBD
            # Traversal strategy: TBD

        # Outputs
            # Optional[TreeNode]: root of our new binary tree