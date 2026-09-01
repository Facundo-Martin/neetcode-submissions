class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # 1-indexed, so we allocate N + 1
        parent = list(range(n + 1)) 

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]] # Path compression
                node = parent[node]
            return node

        for u, v in edges:
            root_u, root_v = find(u), find(v)
            
            if root_u == root_v:
                return [u, v]
            else:
                parent[root_u] = root_v

        return []
            





        