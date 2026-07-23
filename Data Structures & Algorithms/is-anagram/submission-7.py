class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 0. Defensive programming
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for c in countS:
            if countS[S] != countT.get(c):
                return False

        return True        