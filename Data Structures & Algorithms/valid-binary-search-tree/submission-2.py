# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validate_bst_preorder(self, node: Optional[TreeNode], lower_boundary: float, upper_boundary: float) -> bool:
        # Base case: Reached the end of a valid branch
        if not node:
            return True
        
        # Short circuit: Node violates an ancestor's boundary constraint
        if node.val <= lower_boundary or node.val >= upper_boundary:
            return False
        
        # Pre-order DFS: Pass updated boundaries down to left and right children
        validate_left = self.validate_bst_preorder(node.left, lower_boundary, node.val)
        validate_right = self.validate_bst_preorder(node.right, node.val, upper_boundary)
        
        return validate_left and validate_right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Root starts unconstrained (-inf to inf)
        return self.validate_bst_preorder(root, float('-inf'), float('inf'))

    # Dry Run:
        # Tree: 
        #       5
        #      / \
        #     1   6
        #      \
        #       7  <-- The trap (7 is in 5's left subtree, so it MUST be < 5)
        #
        # 1. root (5), allowed: (-infinity to infinity). Valid.
        # 2. Go Left  -> node (1). Update "less than" constraint to parent (5). 
        #    allowed: (-infinity to 5). 1 is valid.
        # 3. Go Right -> node (7). Update "greater than" constraint to parent (1). 
        #    allowed: (1 to 5). 7 is NOT < 5. Short circuit! Return False.

    # Pseudo code:
        # define helper function dfs(node, lower_boundary, upper_boundary):
            # if node is None:
                # return True
            
            # if node.val <= lower_boundary or node.val >= upper_boundary:
                # return False
            
            # validate_left = dfs(node.left, lower_boundary, node.val)
            # validate_right = dfs(node.right, node.val, upper_boundary)
            
            # return validate_left AND validate_right
        
        # main function:
            # return dfs(root, -infinity, infinity)

        
        # Inputs:
            # root: Optional[TreeNode] - The entry point of the binary tree.
            # Edge Case: root is None. An empty tree is mathematically a valid BST. Return True.

        # Constraints:
            # 1. Structural: Left subtree contains ONLY nodes < node.val.
            # 2. Structural: Right subtree contains ONLY nodes > node.val.
            # 3. No duplicates allowed (strictly less than / greater than).

        # Algorithm design:
            # Edge cases:
                # if not node: return True (Reached a leaf's child safely)
            
            # State: 
                # Parent dictates allowed state to its children -> leans towards Pre-order traversal.
                # Must track the constraints set by ancestors as we move down the tree.
                
            # Short circuit:
                # if node.val <= [value of any ancestor it branched right from]: return False
                # if node.val >= [value of any ancestor it branched left from]: return False
            
            # Traversal strategy:
                # BFS (Level-order): Poor fit. Processing horizontally loses vertical subtree boundaries.
                # DFS Post-order (Bottom-up): Clunky. Requires children to calculate min/max and pass UP.
                # DFS In-order (Left-Root-Right): Great fit. Processes nodes sequentially. Valid if strictly increasing.
                # DFS Pre-order (Top-down) -> [CHOSEN]: Best fit for explicit rule enforcement. 
                    # -> Branch Left:  Update the "less than" constraint for the next level.
                    # -> Branch Right: Update the "greater than" constraint for the next level.

        # Outputs:
            # bool: True if the entire tree satisfies all BST constraints, False otherwise.