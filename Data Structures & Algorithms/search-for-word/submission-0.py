class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r: int, c: int, i: int) -> bool:
            # Base Case 1: Out of bounds or character mismatch
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            # Base Case 2: Successfully matched the whole word
            if i == len(word) - 1:
                return True

            # 1. CHOOSE: Mark current cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # 2. EXPLORE: Try the 4 adjacent directions for the next character (i + 1)
            found = (
                backtrack(r - 1, c, i + 1) or  # Up
                backtrack(r + 1, c, i + 1) or  # Down
                backtrack(r, c - 1, i + 1) or  # Left
                backtrack(r, c + 1, i + 1)     # Right
            )

            # 3. UNCHOOSE: Restore original character for other search paths
            board[r][c] = temp

            return found

        # Outer Loop: Try starting the search from every cell on the board
        for r in range(rows):
            for c in range(cols):
                # Small optimization: only launch backtrack if the first letter matches
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True

        return False