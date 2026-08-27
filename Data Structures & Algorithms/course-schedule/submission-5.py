from collections import deque, defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
            
        # 2. Initialize queue with courses that have no prerequisites
        queue = deque()    
        for course in range(numCourses):        
            if in_degree[course] == 0:            
                queue.append(course)
                
        # 3. Process the queue (Kahn's Algorithm)
        completed_courses = 0
        
        while queue:
            current = queue.popleft()
            completed_courses += 1
            
            for dependent in graph[current]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
                    
        return completed_courses == numCourses