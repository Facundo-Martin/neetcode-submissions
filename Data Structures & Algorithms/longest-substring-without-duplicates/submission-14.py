class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            # Add current character to window
            seen.add(s[r])

            # Shrink window from left while duplicate exists
            while s[r] in seen:
                # Remember to update character set! (Before moving l pointer)
                seen.remove(s[l])
                l += 1
            
            # Calculate longest substring once no duplicates are present
            res = max(res, r - l + 1)

        return res

