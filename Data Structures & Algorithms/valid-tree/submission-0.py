class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        # 1. Build Adjacency List
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        
        # 2. Traverse
        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue # Skip the node we just came from
                if neighbor not in visited:
                    dfs(neighbor, node)
                    
        dfs(0, -1) # Start at node 0, parent is -1 (none)
        
        # 3. Did we reach every node?
        return len(visited) == n