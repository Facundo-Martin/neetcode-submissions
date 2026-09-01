class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        # 1-indexed, so we allocate N + 1
        parent = list(range(n + 1))
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]] # Path compression
                node = parent[node]
            return node
            
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            
            # If they share the same boss, we found our cycle!
            if root_u == root_v:
                return [u, v]
                
            # Otherwise, blindly merge them
            parent[root_u] = root_v
            
        return []
