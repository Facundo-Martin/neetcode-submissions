class Solution:
    # Matrix coordinate offsets
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            # Base cases: out of bounds, hit water, already visited island
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] == 0:
                return 0

            # Sink island (we no longer need it)
            grid[r][c] = 0

            # Iterate over coord offsets
            area = 1
            for dr, dc in self.DIRECTIONS:
                area += dfs(r + dr, c + dc)

            return area

        # Search space enumeration
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    new_island_area = dfs(r, c)
                    max_area = max(max_area, new_island_area)

        return max_area




        # Inputs:
            # grid: 2D array, 0s and 1s, non-sorted
                # Bounds: 1 <= rows (M), cols (N) <= 50
                # Max cells (N): M * N = 50 * 50 = 2,500 ≈ 10^3 (order of thousands)

        # Outputs:
            # max_area: int, 0 if no island else largest island area
                # Bounds: 0 <= max_area <= 2,500 ≈ 10^3 (order of thousands)

        # Graph Context:
            # We model this grid as an undirected graph where each cell (r, c) is a node V, 
            # and 4-directional adjacencies are edges E. Because total nodes V = M * N is 
            # physically fixed, our search space is bounded by grid dimensions. 
            # Combinatorial O(2^N) complexity does NOT apply here because we are exploring a 
            # static graph, not generating subsets or decision trees.

        # System constraints:
            # Time complexity:
                # Benchmark: 10^8 ops/sec
                # Naive O(N^2) = O((M*N)^2) ≈ (10^3)^2 = 10^6 ops -> ~0.01s -> Ok, but redundant!
                # Expected O(N) = O(M*N) ≈ 10^3 ops -> <0.001s -> Optimal!
            # Space complexity:
                # General RAM (Universal Baseline):
                    # Benchmark: 256MB (~10^7 elements)
                    # Memory Footprint: O(N) = O(M*N) ≈ 2.5 * 10^3 elements ≈ 0.1MB << 256MB -> Safe!
                # Stack Depth (Recursive DFS Specific):
                    # Benchmark: 10^3 max call frames (Python default recursion limit)
                    # Max Stack Depth: O(N) = O(M*N) ≈ 2.5 * 10^3 frames > 10^3 limit -> Risk of RecursionError!
                    # Mitigation: sys.setrecursionlimit(3000) OR use iterative BFS/DFS.

        # Problem constraints:
            # Value types: grid[i][j] in (0, 1) -> Integers 0 or 1
            # Adjacency Rules: 4-directional adjacency only (Up, Down, Left, Right)
                # Code: DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            # Out-of-Bounds Rules: Out-of-bounds cells are implicitly water (0)
                # Code: if not (0 <= row < rows and 0 <= col < cols): return 0
            # Area Definition: Total count of connected land cells in a component
                # Pseudocode: area = count(all reachable land_cells from (row, col))
            # Spatial Invariant: Cell coordinates (row, col) are fixed; grid cannot be sorted