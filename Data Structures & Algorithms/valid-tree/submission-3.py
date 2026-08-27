from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        # Every node is initially its own parent
        parent = [i for i in range(n)]
        
        # Helper to find the "boss" of a node
        def find(node):
            # We loop until a node is its own parent
            while node != parent[node]:
                parent[node] = parent[parent[node]] # Path compression (optimization)
                node = parent[node]
            return node
            
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            
            # If they share the same root, we just found a cycle
            if root_u == root_v:
                return False
                
            # Merge them: Make u's root the parent of v's root
            parent[root_u] = root_v
            
        return True