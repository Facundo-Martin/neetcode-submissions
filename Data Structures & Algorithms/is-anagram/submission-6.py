class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 0. Defensive programming
        # 1. Create hashmap for first string
        hash1= {}
        hash2 = {}

        for char in s:
            if char in hash1:
                hash1[char] += 1
            hash1[char] = 1

        for char in t:
            if char in hash2:
                hash2[char] += 1
            hash2[char] = 1

        for n in hash1:
            if n not in hash2 or hash1[n] != hash2[n]:
                return False;

        return True        