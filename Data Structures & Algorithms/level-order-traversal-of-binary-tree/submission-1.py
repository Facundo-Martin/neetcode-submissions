# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Short circuit
        if not root:
            return []
            
        ans = []
        queue = deque([root])
        
        while queue:
            # Snapshot of how many nodes are on the current level
            level_size = len(queue)
            current_level = []
            
            # Pop exactly 'level_size' nodes and push their children
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append the grouped level to the final answer
            ans.append(current_level)
            
        return ans
        
        # ===================================
        # Problem Scoping & Algorithm Design
        # ===================================

        # 1. Inputs:
        # root: Binary tree, 0 <= nodes <= 1000, -1000 <= Node.val <= 1000

        # 2. Constraints (Invariants, Edge cases & Short circuits)
        # - "return the level order traversal of it" -> Need to traverse Top-to-bottom, strictly Left-to-Right -> Leaning BFS.
        # - Empty tree (root is None) -> short circuit, return []

        # 3. Patterns & Algo design
        # Leaning BFS for natural level order traversal
            # Recursive BFS: Find height H, loop 1 to H, traverse from root every time to fetch level i.
                # Complexity: O(N^2) Time worst-case, O(N) Space.
            # Iterative BFS with Deque: FIFO structure to process nodes level by level in a single pass.
                # Complexity: O(N) Time (visit each node once), O(N) Space (queue holds max N/2 leaf nodes).
        
        # Hurdle to solve in dry-run: 
        # -> Standard queue BFS gives a flat 1D list. How do we group nodes into a 2D nested list per level?

        # 4. Outputs
        # Nested list [] -> [[level 0], [level 1], ...]