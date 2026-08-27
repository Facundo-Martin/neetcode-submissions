class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def solve(self, board: List[List[str]]) -> None:
        M, N = len(board), len(board[0])
        
        def dfs(r: int, c: int):
            # Base case: Out of bounds OR cell is not an 'O'
            # (This naturally skips 'X' walls and 'T' cells we've already visited)
            if not (0 <= r < M and 0 <= c < N) or board[r][c] != 'O':
                return
            
            # Mutate in-place to mark as safe/visited
            board[r][c] = 'T'
            
            for dr, dc in self.DIRECTIONS:
                dfs(r + dr, c + dc)

        # 1. Seed the DFS from the borders
        for r in range(M):
            if board[r][0] == 'O': dfs(r, 0) # 1st column
            if board[r][N - 1] == 'O': dfs(r, N - 1) # last column
                
        for c in range(N):
            if board[0][c] == 'O': dfs(0, c) # 1st row
            if board[M - 1][c] == 'O': dfs(M - 1, c) # last row

        # 2. Final sweep to clean up the board
        for r in range(M):
            for c in range(N):
                if board[r][c] == 'O':
                    board[r][c] = 'X'   # Unreachable from border -> Trapped
                elif board[r][c] == 'T':
                    board[r][c] = 'O'   # Reachable from border -> Safe