class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            seen = set()

            for j in range(i + 1, n):
                if j in set:
                    break
                
            res = max(res, j - i)
            seen.add(s[j])

        return res
