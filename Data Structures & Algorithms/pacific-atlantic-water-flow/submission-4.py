class Solution:
    # Class attribute: Created once, shared by all instances
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        M, N = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, reachable):
            reachable.add((r, c))
            
            # Access it via self.DIRECTIONS (or Solution.DIRECTIONS)
            for dr, dc in self.DIRECTIONS:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < M and 0 <= nc < N and 
                    (nr, nc) not in reachable and 
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)

        for i in range(M):
            dfs(i, 0, pacific)
            dfs(i, N - 1, atlantic)

        for j in range(N):
            dfs(0, j, pacific)
            dfs(M - 1, j, atlantic)

        return [list(coord) for coord in (pacific & atlantic)]