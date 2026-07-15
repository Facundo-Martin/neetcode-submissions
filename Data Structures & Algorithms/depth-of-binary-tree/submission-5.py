# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # 0 levels in an empty tree
    
        queue = deque([root])
        levels = 0
        
        while queue:
            level_size = len(queue)
            
            # Process every node at the current level
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # We've completely cleared this level, increment the level count
            levels += 1
            
        return levels