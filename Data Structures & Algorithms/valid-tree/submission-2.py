from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set([0])
        queue = deque([(0, -1)]) # (current_node, parent_node)
        
        while queue:
            node, parent = queue.popleft()
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                    
        return len(visited) == n