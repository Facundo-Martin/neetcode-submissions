# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        q = collections.deque([root])
        res = []
        
        while q:
            # The node at the front of the queue is guaranteed to be the rightmost 
            # node of the current level because we push right children first.
            res.append(q[0].val)
            
            level_size = len(q)
            for _ in range(level_size):
                curr = q.popleft()
                
                # Push right child BEFORE left child
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)

        return res
        # ========================================
        # DRY RUN & PSEUDO CODE
        # ========================================

        # --- Pseudo Code ---
        # 1. Edge case: if not root -> return []
        # 2. Init queue = collections.deque([root]), res = []
        # 3. While queue is not empty:
        # 4.     level_length = len(queue)
        # 5.     For _ in range(level_length):
        # 6.         node = queue.popleft()
        # 7.         if node.left: queue.append(node.left)
        # 8.         if node.right: queue.append(node.right)
        # 9.     res.append(node.val)  # The last 'node' processed is the rightmost!
        # 10. Return res

        # --- Dry Run Simulation ---
        # Target Trap Case: Left branch deeper than right
        #       1
        #      / \
        #     2   3
        #    /
        #   4
        #
        # Init: queue=[1], res=[]
        #
        # Level 1 (length=1):
        #   - pop(1), push(2), push(3) -> queue=[2, 3]
        #   - loop ends, last popped node is 1
        #   - res = [1]
        #
        # Level 2 (length=2):
        #   - pop(2), push(4) -> queue=[3, 4]
        #   - pop(3), no children -> queue=[4]
        #   - loop ends, last popped node is 3
        #   - res = [1, 3]
        #
        # Level 3 (length=1):
        #   - pop(4), no children -> queue=[]
        #   - loop ends, last popped node is 4
        #   - res = [1, 3, 4]
        #
        # Queue empty. Return [1, 3, 4]. Algorithm holds.


        # ========================================
        # PROBLEM SCOPING
        # ========================================

        # Inputs
            # root: Optional[TreeNode])
                # 0 <= number of nodes in the tree <= 100 -> Need to deal with not root
                # -100 <= Node.val <= 100 -> Totally fine


        # Constraints
            # "Return only the values of the nodes that are visible from the right side of the tree"
                # -> Need to traverse by level! -> BFS
            # Time complexity: No specific constraint, not sure how On2 would scale compared to On for these values! (0 <= number of nodes in the tree <= 100)
            # Space complexity: No specific constraint
            # Note: Both of these will be conditioned by BFS best practices!!

        # Patterns & Algo design
            # Edge case: No root -> return []
            # Edge case: Left branch is deeper than right branch -> Left nodes become visible!
            # Short circuit: None. Need to traverse entire tree.
            
            # Tree traversal strategy: BFS
                # Option A: Recursive BFS (DFS with level tracking)
                    # Time complexity: O(N) - Must visit every node to check for long left branches
                    # Space complexity: O(H) worst case O(N) - Dictated by call stack depth (tree height)
                # Option B: Iterative BFS (Level-Order Traversal)
                    # Time complexity: O(N) - Must process every node once
                    # Space complexity: O(W) worst case O(N) - Queue holds max width of tree (bottom level)
                    # Data Structure: collections.deque for O(1) popleft() to ensure O(N) time
            
            # Chosen Approach: Iterative BFS


        # Outputs
            # res: 1D array, int, signed, no specific order
            # Null vale? -> Empty list []