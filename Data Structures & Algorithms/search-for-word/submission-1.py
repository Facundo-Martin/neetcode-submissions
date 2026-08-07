class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(r: int, c: int, k: int) -> bool:
            # 1. Failure Guard: Out of bounds or character mismatch
            # Short-circuiting prevents IndexError on board[r][c]
            if not (0 <= r < rows) or not (0 <= c < cols) or board[r][c] != word[k]:
                return False

            # 2. Success Guard: Matched the entire word
            if k == len(word) - 1:
                return True

            # 3. CHOOSE: Temporarily mark cell as visited in-place
            temp = board[r][c]
            board[r][c] = "#"

            # 4. EXPLORE: Iterate through adjacent directions
            for dr, dc in DIRECTIONS:
                if backtrack(r + dr, c + dc, k + 1):
                    board[r][c] = temp  # Restore state before early return
                    return True

            # 5. UNCHOOSE: Restore cell state if no path succeeded
            board[r][c] = temp

            return False

        # Outer loop: Try starting from every cell matching the first letter
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True

        return False