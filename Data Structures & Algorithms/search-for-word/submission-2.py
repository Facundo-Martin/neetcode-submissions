class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()  # Explicit state tracking (Choose -> Explore -> Unchoose)
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(r: int, c: int, i: int) -> bool:
            # Base Case 1: Success (matched full word)
            if i == len(word):
                return True

            # Base Case 2: Failure guard clause
            # (Bounds check + visited check + character mismatch)
            if not (0 <= r < rows) or not (0 <= c < cols) or (r, c) in path or board[r][c] != word[i]:
                return False

            # 1. CHOOSE: Add current coordinate to path state
            path.add((r, c))

            # 2. EXPLORE: Try all 4 directions using directions array
            for dr, dc in DIRECTIONS:
                if backtrack(r + dr, c + dc, i + 1):
                    path.remove((r, c))  # Cleanup before returning True
                    return True

            # 3. UNCHOOSE: Backtrack state
            path.remove((r, c))

            return False

        # Driver loop
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False