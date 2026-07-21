# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Edge case: empty tree
        if not root:
            return 0
            
        good_nodes = 0
        # Stack stores tuples of: (current_node, max_val_so_far)
        # We start with negative infinity so the root is always counted
        stack = [(root, float('-inf'))]
        
        while stack:
            node, max_val = stack.pop()
            
            # 1. Evaluate: Is this a good node?
            if node.val >= max_val:
                good_nodes += 1
                
            # 2. Pack the new briefcase
            new_max = max(max_val, node.val)
            
            # 3. Hand it down to the children
            # (Order of pushing right then left doesn't matter for the final count,
            # but pushing right first makes it traverse left-to-right)
            if node.right:
                stack.append((node.right, new_max))
            if node.left:
                stack.append((node.left, new_max))
                
        return good_nodes
        # Inputs
            # root(TreeNode): 
                # 1 <= number of nodes in the tree <= 100
                # -100 <= Node.val <= 100
            
        # Constraints
            # Good means n > n -1, etc > root
                # Values starting from root are our main blocker
                # Thinking DFS + stack since we are delaying work until we encounter a
                # larger value that will discard all of our work
                # Note: Can/should we do BFS though? Why/why not?

        # Algo design
            # Edge case: just root -> return 1. No root?? Is it possible?
            # Short circuit: None, need to traverse entire tree
            # Traversal strategy: DFS vs BFS, not sure yet
                # [Traversal strategy]
                    # Complexity: 
                    # Data structure:

        # Outputs
            # k: number of good nodes
            # Edge case: Root counts if not null!
            # No res case: return 0
