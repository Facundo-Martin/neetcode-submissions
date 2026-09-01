class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1) # Tracks the size/height of each component
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
            
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            
            if root_u == root_v:
                return [u, v]
                
            # Union by rank: Merge the smaller tree under the larger one
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
                rank[root_u] += rank[root_v]
            else:
                parent[root_u] = root_v
                rank[root_v] += rank[root_u]
                
        return []
