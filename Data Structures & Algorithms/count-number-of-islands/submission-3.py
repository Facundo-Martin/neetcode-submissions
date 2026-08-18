class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(row: int, col: int) -> None:
            # Boundary check & water check
            if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] == '0':
                return
            
            # State mutation: sink the land tile
            grid[row][col] = '0'

            # 4-directional loop using coordinate offsets
            for dr, dc in self.DIRECTIONS:
                dfs(row + dr, col + dc)

        # Search space enumeration
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    island_count += 1
                    dfs(row, col)

        return island_count
        
        # Inputs: 
            # grid: 2D array, strings, restricted strings "0" & "1"
                # Bounds: 1 <= grid.length (rows, M), grid[i].length (cols, N) <= 100
                # Max cells (N): M * N = 100 * 100 = 10^4

        # Outputs:
            # ans: Unsigned int, number of distinct connecting adjacent lands
                # Bounds: 0 <= ans <= 5,000 (checkerboard pattern: 1 0 1 0...)
        
        # System constraints:
            # Time complexity: 
                # Benchmark: 10^8 ops/sec
                # Naive O(N^2) = O((M*N)^2) = O((10^4)^2) = 10^8 ops = 1s -> Borderline TLE!
                # Expected O(N) = O(M*N) = O(10^4) = 10^4 ops = <0.01s -> Ok!
            # Space complexity:
                # Expected O(N) = O(M*N) auxiliary space is acceptable

        # Problem constraints:
            # 1. grid[i][j] is '0' or '1'
            # 2. Adjacent connecting '1's count as a single island
            # 3. We can only connect lands horizontally or vertically
                # For every grid[i][j] coord, valid adj coords are: 
                # [(1, 0), (0, 1), (0, -1), (-1, 0)], taking [i][j] as center (0,0)
            # 4. We may assume water is surrounding the grid (i.e., all the edges are water)
                # if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]): return

        # Algorithm design
            # Goal: Enumerate all valid islands in our search space 
            # Identity: Matrix Traversal + Graph Connected Components (Flood Fill)
            # Strategies:
                # 1. DFS (Depth-First Search)
                # 2. BFS (Breadth-First Search)
                # 3. Disjoint Set / Union-Find
            # Chosen strategy: DFS
            # Failure mode: 
                # 1. Infinite loops/double-counting if we fail to mark '1's as visited.
                # 2. Recursion depth limit exceeded.
            # Edge cases: Grid is entirely '0's, grid is entirely '1's, 1x1 grid.
            # Base cases:
                # 1. Pointer goes out of bounds.
                # 2. Current pointer is at '0'.


            # The only tiny question a top-tier interviewer might ask is: "Are we allowed to mutate the input grid, or is it read-only?" (If read-only, you must use a separate $O(M \times N)$ visited set/matrix). Other than that, this scoping is senior-engineer level.