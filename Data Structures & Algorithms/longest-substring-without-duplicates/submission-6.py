class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            seen = set()

            for j in range(i + 1, n):
                if n[j] in seen:
                    break
                
                res = max(res, j - i + 1)
                seen.add(s[j])

        return res
