class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) # Dimensions of rows and cols
        minutes = 0
        fresh_count = 0

        q = deque()

        # 1. Enqueue all rotten fruits & count fresh ones
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c)) # Append coordinates of rotten fruit
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Edge case: No fresh oranges to begin with
        if fresh_count == 0:
            return 0

        while q and fresh_count > 0:
            minutes += 1

            # Process strictly the current minute's boundary
            for _ in range(len(q)):
                r, c = q.popleft()

                # Grab all potential neighbors
                for dr, dc in self.DIRECTIONS:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and 0 <= nc < n) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mutate in-place to avoid duplicate queuing
                        fresh_count -= 1
                        q.append((nr, nc))
                


        return minutes if fresh_count == 0 else -1


        # Inputs:
            # grid: 2D array, 0s, 1s, and 2s, non-sorted
                # Bounds: 1 <= rows (M), cols (N) <= 10
                # Max cells (N): M * N = 10 * 10 = 100 ≈ 10^2

        # Outputs:
            # minutes: int, minimum minutes to rot all oranges, or -1 if impossible
                # Bounds: -1 <= minutes <= 100

        # Problem constraints:
            # Value types: grid[r][c] in (0, 1, 2) -> Integers for empty, fresh, and rotten
            # Adjacency Rules: 4-directional adjacency only (Up, Down, Left, Right)
                # Code: DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            # Out-of-Bounds Rules: Out-of-bounds cells are implicitly empty (0)
                # Code: if not (0 <= r < m and 0 <= c < n): continue
            # State transitions: 1 (fresh) -> 2 (rotten) when adjacent to a rotten cell
            # Spatial Invariant: Cell coordinates (row, col) are fixed; grid cannot be sorted.

        # System constraints:
            # Time complexity:
                # Benchmark: 10^8 ops/sec
                # Expected O(N) = O(M*N) = 10^2 ops -> <0.00001s -> Optimal! 
                # (Every cell is enqueued/processed at most once).
            # Space complexity:
                # General RAM (Universal Baseline):
                    # Benchmark: 256MB (~10^7 elements)
                    # Memory Footprint: O(N) = O(M*N) ≈ 100 elements << 256MB -> Safe!
                # Queue Depth (Iterative BFS):
                    # Max Queue Size: O(N) = 100 elements -> Negligible overhead.

        # Algorithm design
            # Goal: Find the minimum time required to infect all fresh oranges, or determine if it's impossible.
            # Identity: Matrix Traversal + Multi-Source Shortest Path (Level-Order Traversal)
                # Why: We need to traverse an implicit 2D grid graph radiating outward 
                # simultaneously from MULTIPLE initial origin nodes (rotten oranges), tracking time/distance.
            # Strategies:
                # 1. Multi-source BFS - Ideal for unweighted shortest path/time. Processes layer-by-layer uniformly.
                # 2. DFS - Poor fit. Requires tracking minimum timestamps at every cell and heavy re-traversals.
            # Chosen strategy: Iterative Multi-Source BFS (Queue-based, processing by level size)
            # Failure modes: 
                # 1. Forgetting to count the initial number of fresh oranges, making it impossible 
                #    to efficiently verify if unreachable ones remain at the end.
                # 2. Popping nodes without a level-size inner loop, leading to inaccurate minute tracking.
            # Edge cases: 
                # 1. Grid has no fresh oranges initially -> returns 0.
                # 2. Grid has fresh oranges but no rotten oranges initially -> returns -1.
            # Base cases (Validation & Boundaries):
                # 1. Pointer goes out of bounds -> ignore neighbor.
                # 2. Neighbor is not a fresh orange (grid != 1) -> ignore neighbor
