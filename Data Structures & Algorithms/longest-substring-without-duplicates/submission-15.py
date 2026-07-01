class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            # Shrink window from left while duplicate exists
            while s[r] in seen:
                # Remember to update character set! (Before moving l pointer)
                seen.remove(s[l])
                l += 1
            
            # Add custom logic once there are no duplicates
            res = max(res, r - l + 1)
            seen.add(s[r])

        return res

