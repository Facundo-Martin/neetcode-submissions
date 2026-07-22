# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes_visited= 0
        target_value= 0 

        def dfs_in_order(node: Optional[TreeNode]) -> None:
            nonlocal nodes_visited, target_value
            
            # Base case & short-circuit: stop if node is null or we already hit k
            if not node or nodes_visited == k:
                return
            
            # 1. Traverse Left (Left)
            dfs_in_order(node.left)
            
            # 2. Process Current Node (Node)
            nodes_visited += 1
            if nodes_visited == k:
                target_value = node.val
                return  # Short-circuit further processing on this branch
                
            # 3. Traverse Right (Right)
            dfs_in_order(node.right)

        # Kick off the traversal
        dfs_in_order(root)
        
        return target_value

    # Inputs
        # root: root of binary search tree
        # k: the target rank of the smallest integer

    # Constraints
        # 1 <= k <= nodes <= 1000
        # Tree is guaranteed to have at least 1 node (root is never None)
        # Standard BST properties apply (Left < Node < Right)

    # Patterns & Algo design
        # Traversal choice: DFS In-order (Left, Node, Right). 
            # Why? Because In-order traversal of a BST visits nodes in perfectly
            # sorted ascending order.
        # State tracking: 
            # Need an integer to track `nodes_visited`.
            # Need a variable to store the `result` once found.
        # Short circuit:
            # Once `nodes_visited == k`, we record the value and stop unnecessary traversals.

    # Pseudo code
        # 1. Initialize `nodes_visited = 0` and `result = None`
        # 2. Define DFS In-order helper function:
            # Base case: if node is None or result is already found (short circuit), return
            # Traverse Left: dfs(node.left)
            # Process Node: 
                # nodes_visited += 1
                # if nodes_visited == k: result = node.val, return
            # Traverse Right: dfs(node.right)
        # 3. Call dfs(root)
        # 4. Return result

            