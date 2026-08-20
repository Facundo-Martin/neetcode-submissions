
class Solution:
    # Class-level constants
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return



        m, n = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addRoom(r:int, c: int) -> None:
            # Edge cases: Out of bounds, water (can't traverse)
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] == -1 or (r, c) in visited:
                return
            
            visited.add((r,c))
            q.append([r, c])
            
 
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append([r, c]) # Enqueue coordinates
                    visited.add((r, c)) # Add tuple to visited set

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                grid[r][c] = dist

                for dr, dc in self.DIRECTIONS:
                    addRoom(r + dr, c + dc)
            
            dist += 1

        

                