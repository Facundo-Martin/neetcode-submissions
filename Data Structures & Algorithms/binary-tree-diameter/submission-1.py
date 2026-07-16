# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       # This is our global "record book" to keep track of the longest path.
        self.max_diameter = 0
        
        def calculate_height(node):
            # BASE CASE: If we hit a null node, its height is 0.
            if not node:
                return 0
            
            # STEP 1: Dive all the way to the bottom.
            # We don't calculate anything until we reach the leaves.
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
            
            # STEP 2: The Magic "Two-in-One" Step!
            # While we are standing at this node, we instantly know its left and right heights.
            # We add them together to get the diameter at this node, and update our record book.
            current_diameter = left_height + right_height
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # STEP 3: Return the height of this node to its parent.
            # We tell the parent: "Hey, my height is 1 plus whichever of my subtrees is taller."
            return 1 + max(left_height, right_height)
        
        # Start the bottom-up process from the root
        calculate_height(root)
        
        # After visiting every node exactly once, our record book holds the winner!
        return self.max_diameter