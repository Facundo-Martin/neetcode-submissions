class Solution:
    def validPalindrome(self, s: str) -> bool:
        r, l = 0, len(s) - 1
        removed = []

        while r < l:
            # Handle matching characters (base case / happy path)
            if s[r] == s[l]:
                r += 1
                l -= 1
            # Handle non-matching characters
            else:
                # No charecters left to remove
                if len(removed) > 0:
                    return False
                
                else: 
                # Right character is removable
                    if s[r + 1] == s[l]: 
                        removed.append(s[r])
                        r += 1 
                        continue
                # Left character is removable
                    elif s[r] == s[l - 1]: 
                        removed.append(s[l])
                        l -= 1 
                        continue

        return True
        