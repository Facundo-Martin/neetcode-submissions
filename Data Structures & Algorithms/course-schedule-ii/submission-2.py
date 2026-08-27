class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Initialize queue with courses having no prerequisites
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        # Process courses in topological order
        result = []
        
        while queue:
            current = queue.popleft()
            result.append(current)
            
            # Reduce in-degree for dependent courses
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if all courses were processed (no cycle)
        if len(result) == numCourses:
            return result
        else:
            return []