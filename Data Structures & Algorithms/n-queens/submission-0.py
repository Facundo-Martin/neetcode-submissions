from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        
        # Track occupied attack lines
        occupied_cols = set()      # Column indices
        occupied_pos_diag = set()  # (row + col)
        occupied_neg_diag = set()  # (row - col)
        
        # The board state: an n x n grid initialized with '.'
        state = [["."] * n for _ in range(n)]

        def backtrack(row: int):
            # Base case: successfully placed a queen in every row
            if row == n:
                formatted_board = ["".join(r) for r in state]
                results.append(formatted_board)
                return

            for col in range(n):
                # Skip if column or diagonals are under attack
                if (col in occupied_cols or 
                    (row + col) in occupied_pos_diag or 
                    (row - col) in occupied_neg_diag):
                    continue

                # 1. Apply choice
                occupied_cols.add(col)
                occupied_pos_diag.add(row + col)
                occupied_neg_diag.add(row - col)
                state[row][col] = "Q"

                # 2. Recurse to the next row
                backtrack(row + 1)

                # 3. Undo choice (backtrack)
                occupied_cols.remove(col)
                occupied_pos_diag.remove(row + col)
                occupied_neg_diag.remove(row - col)
                state[row][col] = "."

        backtrack(row=0)
        return results