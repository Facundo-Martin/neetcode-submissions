# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _dfs(self, node: Optional[TreeNode], level: int, res: List[List[int]]) -> None:
        # Base case
        if not node:
            return
            
        # If this is the first time we've reached this level, create a new sublist for it
        if len(res) == level:
            res.append([])
            
        # Add the current node's data to its corresponding level
        res[level].append(node.val)
        
        # Traverse left, then right, passing down the incremented level
        self._dfs(node.left, level + 1, res)
        self._dfs(node.right, level + 1, res)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self._dfs(root, 0, res)
        return res
        
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