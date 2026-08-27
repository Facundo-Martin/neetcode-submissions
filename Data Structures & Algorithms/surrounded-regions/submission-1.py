class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def solve(self, board: List[List[str]]) -> None:
        M, N = len(board), len(board[0])
        visited = set() # Keep track of visited coordinates
        
        def dfs(r: int, c: int):
            # Base case: Out of bounds, already visited, or hit a wall ('X')
            if not (0 <= r < M and 0 <= c < N) or (r, c) in visited or board[r][c] == 'X':
                return
            
            visited.add((r, c))
            
            for dr, dc in self.DIRECTIONS:
                dfs(r + dr, c + dc)

        # 1. Seed the DFS from the borders
        for r in range(M):
            if board[r][0] == 'O' and (r, 0) not in visited:
                dfs(r, 0)         # Left column
            if board[r][N - 1] == 'O' and (r, N - 1) not in visited:
                dfs(r, N - 1)     # Right column
                
        for c in range(N):
            if board[0][c] == 'O' and (0, c) not in visited:
                dfs(0, c)         # Top row
            if board[M - 1][c] == 'O' and (M - 1, c) not in visited:
                dfs(M - 1, c)     # Bottom row

        # 2. Final sweep to flip surrounded 'O's
        for r in range(M):
            for c in range(N):
                # If it's an 'O' but the boundary DFS never reached it, it's trapped.
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'