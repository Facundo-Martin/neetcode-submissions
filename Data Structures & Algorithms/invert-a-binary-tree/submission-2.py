# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      from collections import deque

def invertTreeIterative(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        
        # Swap the children of the current node
        current.left, current.right = current.right, current.left
        
        # Add the children to the queue if they exist
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            
    return root