class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        for i in range(n - m + 1):
            substring = s2[i: i + m]

            if sorted(substring) == sorted(s1):
                return True

        return False