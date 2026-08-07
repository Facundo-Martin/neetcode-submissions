class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        state = []

        def dfs(i):
            if i >= len(s):
                res.append(state.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    state.append(s[i : j + 1])
                    dfs(j + 1)
                    state.pop()

        dfs(0)
        return res

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True