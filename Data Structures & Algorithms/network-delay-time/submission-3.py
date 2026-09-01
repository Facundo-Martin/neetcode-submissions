import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # 1. Build your preferred array-based adjacency list
        # We use n + 1 so the index perfectly matches the 1-indexed nodes
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))
            
        # 2. Min-Heap stores tuples of (accumulated_time, node)
        min_heap = [(0, k)]
        visited = set()
        
        # Tracks the time it takes for the LAST node to receive the signal
        total_time = 0
        
        while min_heap:
            current_time, node = heapq.heappop(min_heap)
            
            # The Lazy check: if we already popped this node earlier, 
            # we already found a faster path. Throw this slower one away.
            if node in visited:
                continue
                
            # The first time we pop a node, we lock it in
            visited.add(node)
            total_time = current_time # Automatically tracks max time since heap is strictly increasing
            
            # Push all unvisited neighbors into the heap
            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (current_time + weight, neighbor))
                    
        # 3. Did the signal reach all 'n' nodes?
        return total_time if len(visited) == n else -1
