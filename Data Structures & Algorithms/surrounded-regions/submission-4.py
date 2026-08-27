from collections import deque
from typing import List

class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
            
        M, N = len(board), len(board[0])
        queue = deque()

        # 1. Seed the queue with all border 'O's and mark them 'T' instantly
        for r in range(M):
            if board[r][0] == 'O':
                queue.append((r, 0))
                board[r][0] = 'T'
            if board[r][N - 1] == 'O':
                queue.append((r, N - 1))
                board[r][N - 1] = 'T'
                
        for c in range(N):
            if board[0][c] == 'O':
                queue.append((0, c))
                board[0][c] = 'T'
            if board[M - 1][c] == 'O':
                queue.append((M - 1, c))
                board[M - 1][c] = 'T'

        # 2. Multi-source BFS to spread the 'T' marker inwards
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in self.DIRECTIONS:
                nr, nc = r + dr, c + dc
                # If neighbor is valid and is an 'O'
                if 0 <= nr < M and 0 <= nc < N and board[nr][nc] == 'O':
                    board[nr][nc] = 'T'
                    queue.append((nr, nc))

        # 3. Final Sweep
        for r in range(M):
            for c in range(N):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'