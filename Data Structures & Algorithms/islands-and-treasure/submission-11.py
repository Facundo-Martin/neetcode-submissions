class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    INF = 2147483647

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        m, n = len(grid), len(grid[0])
        queue = deque()

        # 1. Collect all treasure chests to start BFS concurrently
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # 2. Continuous BFS expansion
        while queue:
            r, c = queue.popleft()

            for dr, dc in self.DIRECTIONS:
                nr, nc = r + dr, c + dc

                # An empty land cell is strictly equal to INF.
                # If it's already an integer < INF, it was already visited by a closer chest.
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == self.INF:
                    # Write the distance directly upon discovery
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))