# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        
        def dfs(node):
            if not node:
                vals.append("N")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(vals)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        # Create an iterator from our list of strings
        vals_iterator = iter(data.split(","))
        
        def dfs():
            # Get the next value in the sequence
            val = next(vals_iterator)
            
            if val == "N":
                return None
                
            # Pre-order: Root first, then left, then right
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()

    # Inputs:
        # serialize: root (Optional[TreeNode]) - The entry point of the binary tree.
        # deserialize: data (str) - The comma-separated string representation of the tree.
        # Edge Case: root is None. Return "N".
        # Edge Case: data is "N". Return None.

    # Constraints:
        # 1. Structural: The deserialized tree must be identical to the original tree.
        # 2. Values: Nodes can contain negative integers or multi-digit numbers (must use delimiters).
        # 3. State: The algorithm cannot rely on global variables across multiple calls.

    # Algorithm design:
        # Edge cases:
            # If tree is empty, we must still serialize it as something (e.g., "N") so 
            # deserialize knows to return None.
        
        # State: 
            # Rebuilding a tree requires knowing exactly which string value we are currently 
            # looking at. We need an Iterator or a pointer that moves forward sequentially 
            # and never goes backward.
            
        # Short circuit / Trimming:
            # If the current value is "N", we immediately return None. We don't try to build 
            # children for a null node.
        
        # Traversal strategy:
            # BFS (Level-order): Good fit. Works visually left-to-right, but requires 
            # managing a queue for both serialization and deserialization.
            # DFS In-order (Left-Root-Right): Fatal flaw. The root gets buried in the middle 
            # of the string. Without knowing the size of the left branch in advance, it is 
            # impossible to locate the root when reading the string left-to-right. 
            # DFS Post-order (Left-Right-Root): Ergonomic flaw. It puts the root at the very 
            # end. While technically possible if we read the string backwards (Root-Right-Left),
            # it forces us to unnaturally rebuild the right side of the tree before the left.
            # DFS Pre-order (Root-Left-Right) -> [CHOSEN]: Perfect fit. Maps cleanly to reading 
            # a string left-to-right and naturally building top-down, left-to-right.

        
