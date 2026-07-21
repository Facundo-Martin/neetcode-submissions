# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self._dfs(root, float('-inf'))

    def _dfs(self, node: TreeNode, max_val: float) -> int:
        # Base case
        if not node:
            return 0
            
        # 1. Evaluate
        count = 1 if node.val >= max_val else 0
        
        # 2. Pack the new state
        new_max = max(max_val, node.val)
        
        # 3. Hand it down and aggregate
        count += self._dfs(node.left, new_max)
        count += self._dfs(node.right, new_max)
        
        return count
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
