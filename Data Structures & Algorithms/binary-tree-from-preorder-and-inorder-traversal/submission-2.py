# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # O(1) lookup for inorder indices
        inorder_index_map = {value: index for index, value in enumerate(inorder)}

        def build_subtree(preorder_start: int, inorder_start: int, subtree_size: int) -> Optional[TreeNode]:
            if subtree_size <= 0:
                return None

            # Current root is always the first element in the preorder window
            root_value = preorder[preorder_start]
            root_inorder_index = inorder_index_map[root_value]
            left_subtree_size = root_inorder_index - inorder_start
            
            # Recursively build left subtree
            left_child = build_subtree(
                preorder_start + 1, 
                inorder_start, 
                left_subtree_size
            )
            
            # Recursively build right subtree
            right_child = build_subtree(
                preorder_start + 1 + left_subtree_size,
                root_inorder_index + 1,
                subtree_size - left_subtree_size - 1
            )
            
            # Create and return the root node with its children
            return TreeNode(root_value, left_child, right_child)

        return build_subtree(0, 0, len(preorder))
        
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