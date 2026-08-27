class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build the adjacency list
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)
            
        # state array: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def has_cycle(node: int) -> bool:
            if state[node] == 1:
                return True  # Walked back into our current path = Cycle!
            if state[node] == 2:
                return False # Already cleared this node in a previous DFS
                
            state[node] = 1  # Mark as visiting
            
            for neighbor in adj[node]:
                if has_cycle(neighbor):
                    return True
                    
            state[node] = 2  # Mark as safe/visited
            return False
            
        # 2. Check every course (required because the graph might be disconnected)
        for i in range(numCourses):
            if state[i] == 0:
                if has_cycle(i):
                    return False
                    
        return True