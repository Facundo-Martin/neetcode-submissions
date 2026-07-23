# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        global_max = float('-inf')
        
        def get_max_gain(node):
            # Base case: empty node contributes 0
            if not node:
                return 0
            
            # Recursively get maximum gain from left and right subtrees
            # Maximize gains using Use max(0, ...) to ignore negative paths
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Calculate the maximum path sum that passes through the current node
            current_path_sum = node.val + left_gain + right_gain
        
            # Update the global maximum path sum if current path is better
            nonlocal global_max
            global_max = max(global_max, current_path_sum)
            
            # Return the maximum gain when continuing the path through parent
            # We can only pick one branch (left or right) when going through parent
            return node.val + max(left_gain, right_gain)
            
        get_max_gain(root)
        
        return global_max

    # Inputs:
        # root: Optional[TreeNode] - The entry point of the binary tree.
        # Edge Case: root is None. Return 0.
        # Edge Case: Tree has only negative numbers. 

    # Constraints:
        # 1. Structural: A path must be a continuous sequence of connected nodes.
        # 2. Structural: A path can go up to a parent and down to one child (an inverted 'V'), but it CANNOT branch.
        # 3. Values: Nodes can contain negative integers.

    # Algorithm design:
        # Edge cases:
            # if not node: return 0 (An empty branch contributes nothing to the sum).
            # Initialize global max to float('-inf') to handle all-negative trees.
        
        # State: 
            # Parent needs answers from children before it can calculate its own max -> Bottom-up flow.
            # Need a global/nonlocal state to track the absolute highest 'V' shape seen anywhere.
            
        # Short circuit / Trimming:
            # If a child's best straight-line path is negative, it hurts the sum. 
            # Trim it instantly: max(child_gain, 0).
        
        # Traversal strategy:
            # BFS (Level-order): Poor fit. Destroys vertical path continuity.
            # DFS Pre-order (Top-down): Poor fit. Parent doesn't know child path sums yet.
            # DFS In-order (Left-Root-Right): Poor fit. Flattening destroys parent-child branching rules.
            # DFS Post-order (Bottom-up) -> [CHOSEN]: Best fit. 
                # -> Get left max, get right max.
                # -> Calculate 'V' shape and update global state.
                # -> Return straight line to parent.

    # Pseudo code:
        # define main function maxPathSum(root):
            # global_max = -infinity
            
            # define helper function get_max_gain(node):
                # nonlocal global_max
                
                # if node is None: return 0
                
                # left_gain = max(get_max_gain(node.left), 0)
                # right_gain = max(get_max_gain(node.right), 0)
                
                # current_v_path = node.val + left_gain + right_gain
                # global_max = max(global_max, current_v_path)
                
                # return node.val + max(left_gain, right_gain)
                
            # get_max_gain(root)
            # return global_max

    # Dry Run:
        # Tree: 
        #       -10
        #       /  \
        #      9   20
        #         /  \
        #       15    7
        #
        # 1. Post-order goes all the way down. 
        # 2. Node(15) returns 15. Node(7) returns 7.
        # 3. Node(20) receives 15 and 7. 
        #    -> 'V' shape check: 20 + 15 + 7 = 42. (global_max = 42).
        #    -> Returns to parent: 20 + max(15, 7) = 35.
        # 4. Node(9) returns 9.
        # 5. Node(-10) receives 9 and 35.
        #    -> 'V' shape check: -10 + 9 + 35 = 34. (34 is less than 42, ignore).
        #    -> Returns to parent: -10 + max(9, 35) = 25.
        # 6. Traversal ends. Return global_max (42).

    # Outputs:
        # int: The highest possible sum of any valid path in the tree.
        