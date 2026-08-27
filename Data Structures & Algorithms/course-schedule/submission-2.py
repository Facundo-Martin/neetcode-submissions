from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build the adjacency list and in-degree array
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
            
        # 2. Queue up all courses that have 0 prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed_courses = 0
        
        # 3. Process the queue
        while queue:
            current = queue.popleft()
            completed_courses += 1
            
            # When we "take" a course, its neighbors require one less prerequisite
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                # If a neighbor has no more prerequisites, it's ready to take
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If we took all courses, there was no cycle
        return completed_courses == numCourses