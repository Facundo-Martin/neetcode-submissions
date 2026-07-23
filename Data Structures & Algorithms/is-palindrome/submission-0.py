class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.trim()
        if len(s) == 0:
            return False

        l, r = 0, len(s) - 1

        ans = True

        while l < r:
            if s[l] != s[r]:
                ans = False
                break

        return ans


        