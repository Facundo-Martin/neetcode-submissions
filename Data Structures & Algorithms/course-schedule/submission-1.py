from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build graph: course -> list of prerequisites
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        # Explicit state definitions
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            
            # Base cases for state
            if state == VISITED: 
                return True
            elif state == VISITING: 
                return False

            # Mark the current node as in-progress
            states[node] = VISITING

            # Traverse prerequisites
            for nei in g[node]:
                if not dfs(nei): 
                    return False
            
            # Mark the node as fully processed and cycle-free
            states[node] = VISITED
            return True
        
        # Initiate DFS for every course (handles disconnected graphs)
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True