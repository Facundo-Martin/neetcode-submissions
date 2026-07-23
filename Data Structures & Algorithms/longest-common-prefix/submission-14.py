class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for i, ch in enumerate(len(strs[0])): # Grab a random string
            for s in strs:  
                if i >= len(s): # Handle out of bounds scenario
                    return ans
                if ch != s[i]:
                    return ans

            ans += ch

        return ans
            