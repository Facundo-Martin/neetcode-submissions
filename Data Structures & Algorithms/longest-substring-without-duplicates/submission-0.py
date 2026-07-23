class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0

        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == j[i]:
                    curr_length = j - i
                    longest = max(longest, curr_length)

        return longest
