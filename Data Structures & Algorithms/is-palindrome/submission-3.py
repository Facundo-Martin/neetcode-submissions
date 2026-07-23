class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(str) - 1

        while l < r:
            while not self.isAlphaNum(s[l]) and l < r:
                l += 1
            while not self.isAlphaNum(s[r]) and r > l:
                r -= 1
            # Do logic
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True
    
    def isAlphaNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9') )


        