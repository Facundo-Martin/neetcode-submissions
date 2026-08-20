class Solution:
    # Direction vectors for navigating: [Down, Up, Right, Left]
    # dr = delta row, dc = delta col
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    INF = 2147483647

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        m, n = len(grid), len(grid[0])
        queue = deque()

        # 1. Enqueue all chest coordinates (distance 0 baseline)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # 2. Ripple BFS outward
        while queue:
            r, c = queue.popleft()
            curr_dist = grid[r][c]  # Current validated distance

            for dr, dc in self.DIRECTIONS:
                nr, nc = r + dr, c + dc

                # Only move onto traversable land that hasn't been claimed yet
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == self.INF:
                    grid[nr][nc] = curr_dist + 1
                    queue.append((nr, nc))