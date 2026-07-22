# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# "Alright, so this recursive approach works perfectly and gives us $O(N)$ time and $O(H)$ space. If we are dealing with a relatively balanced BST, I'd ship this because closures in Python are clean and easy to read.However, if we deployed this to production and someone fed it a highly skewed tree—like 5,000 nodes linked entirely to the left—this would blow up the Python call stack and throw a RecursionError. The invisible call stack simply can't handle it.If we need this to be totally bulletproof for massive, unbalanced datasets, I'd rewrite this iteratively using a manual array as a stack. It moves the memory overhead from the call stack to the heap, which scales much better. We have some time left—would you like me to code out the iterative stack version?"

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        # Keep running as long as there are nodes to process
        # or we are currently looking at a valid node
        while curr or stack:
            
            # 1. Dive as deep left as physically possible
            # This guarantees the smallest elements are pushed to the top of the stack
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # 2. Process the smallest available node (top of the stack)
            curr = stack.pop()
            k -= 1
            
            # 3. Short-circuit if we hit our target
            if k == 0:
                return curr.val
                
            # 4. Shift right to explore larger elements
            curr = curr.right

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

            