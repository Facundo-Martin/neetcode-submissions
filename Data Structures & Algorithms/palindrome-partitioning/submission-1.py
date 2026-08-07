class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        state = []  # Scoped alongside results in the outer function

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start_idx: int):
            # Base Case: Reached the end of the string
            if start_idx == len(s):
                results.append(state.copy())  # Snapshot the valid path
                return

            # Available choices: every possible split index for the current substring
            for split_idx in range(start_idx, len(s)):
                substring = s[start_idx : split_idx + 1]

                # PRUNING: Only explore valid palindromes
                if is_palindrome(substring):
                    # 1. CHOOSE
                    state.append(substring)

                    # 2. EXPLORE
                    backtrack(split_idx + 1)

                    # 3. UNCHOOSE
                    state.pop()

        backtrack(0)
        return results