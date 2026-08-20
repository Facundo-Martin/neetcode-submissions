from collections import deque
from typing import List

class Solution:
    # Class-level constants
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """
        if not grid or not grid[0]:
            return

        m, n = len(grid), len(grid[0])
        visited = set()
        q = deque()

        # Helper function: validates boundaries, obstacles, and visited state
        def addRoom(r: int, c: int) -> None:
            # 1. Bounds check (must satisfy BOTH 0 <= r < m AND 0 <= c < n)
            # 2. Obstacle check (water / walls marked as -1)
            # 3. Cycle prevention (already visited)
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] == -1 or (r, c) in visited:
                return

            # Mark as visited immediately to prevent duplicate queue entries
            visited.add((r, c))
            q.append((r, c))

        # 1. Multi-source initialization: enqueue all treasure chests (distance 0)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        # 2. Level-by-level BFS expansion
        dist = 0
        while q:
            # Snapshot: process only nodes belonging to current distance level
            for _ in range(len(q)):
                r, c = q.popleft()

                # Write the confirmed shortest distance to the current cell
                grid[r][c] = dist

                # Check all 4 neighbors using class constant DIRECTIONS
                for dr, dc in self.DIRECTIONS:
                    addRoom(r + dr, c + dc)

            # Increment distance after completing the current layer
            dist += 1