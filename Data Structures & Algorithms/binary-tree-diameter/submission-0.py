# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, node: TreeNode) -> int:
        # Base case: We run off the bottom of the tree (reach a null child), return 0
        if not node:
            return 0
        
        # --- HEIGHT STEP 2: The Downward Dive ---
        # We must dive all the way to the bottom of the left and right subtrees 
        # before we can calculate the height of the current node.
        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)

        # --- HEIGHT STEP 3: The Upward Count ---
        # Once we know the heights of both sides, we choose the taller one 
        # and add 1 (representing the current node itself) to pass back up.
        return 1 + max(left_height, right_height)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Base Case: An empty tree has a diameter of 0.
        if not root:
            return 0
        
        # =================================================================
        # PHASE A: Calculate the diameter THROUGH the current node (e.g., Root)
        # =================================================================
        
        # 1. We pause here and launch 'getHeight'. 
        #    This travels all the way down the left side of 'root'.
        left_height = self.getHeight(root.left)
        
        # 2. We pause again and launch 'getHeight'.
        #    This travels all the way down the right side of 'root'.
        right_height = self.getHeight(root.right)
        
        # 3. This is the max path length *if* this current node is the turning point.
        current_diameter = left_height + right_height
        
        # =================================================================
        # PHASE B: The Recursive "Step Down" (Top-to-Bottom traversal)
        # =================================================================
        
        # 4. We now step down to the LEFT child and run 'diameterOfBinaryTree' 
        #    on it. This is where Phase A starts all over again for the left child!
        left_diameter = self.diameterOfBinaryTree(root.left)
        
        # 5. After the left side is completely done, we step down to the RIGHT 
        #    child and run 'diameterOfBinaryTree' on it. Phase A starts again here.
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        # =================================================================
        # PHASE C: The Decision
        # =================================================================
        
        # 6. Finally, we compare:
        #    - Did the longest path turn at the current root? (current_diameter)
        #    - Or was there a better path completely inside the left family tree? (left_diameter)
        #    - Or completely inside the right family tree? (right_diameter)
        return max(current_diameter, left_diameter, right_diameter)