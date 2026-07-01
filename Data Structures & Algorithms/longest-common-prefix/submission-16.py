class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i, ch in enumerate(min(strs, key=len)):
            for s in strs:
                if s[i] != ch:
                    return prefix
            prefix += ch

        return prefix