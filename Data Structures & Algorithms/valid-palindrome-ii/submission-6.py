class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        removed = False

        while l < r:

            # Happy path
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue

            # Already removed one character
            if removed:
                return False

            removed = True

            # Skip left character
            if s[l + 1] == s[r]:
                l += 1

            # Skip right character
            elif s[l] == s[r - 1]:
                r -= 1

            # Neither works
            else:
                return False

        return True