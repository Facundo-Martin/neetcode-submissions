class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for i in range (len(strs[0])): # Grab a random string
            for s in strs:  
                if i >= len(s): # Handle out of bounds scenario
                    return ans
                if strs[0][i] != s[i]:
                    return ans

        return ans
            