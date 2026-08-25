from collections import deque

class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        M, N = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        p_queue = deque()
        a_queue = deque()

        # Seed the left and right borders
        for i in range(M):
            p_queue.append((i, 0))
            pacific.add((i, 0))
            a_queue.append((i, N - 1))
            atlantic.add((i, N - 1))

        # Seed the top and bottom borders
        for j in range(N):
            p_queue.append((0, j))
            pacific.add((0, j))
            a_queue.append((M - 1, j))
            atlantic.add((M - 1, j))

        def bfs(queue, reachable):
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in self.DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    
                    if (0 <= nr < M and 0 <= nc < N and 
                        (nr, nc) not in reachable and 
                        heights[nr][nc] >= heights[r][c]):
                        
                        reachable.add((nr, nc))
                        queue.append((nr, nc))

        bfs(p_queue, pacific)
        bfs(a_queue, atlantic)

        # The optimized intersection
        return [list(coord) for coord in (pacific & atlantic)]