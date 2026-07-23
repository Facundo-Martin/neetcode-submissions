class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        mid = len(s) / 2

        while l < mid and r > mid:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
        
        