class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 0. Defensive programming
        # 1. Create hashmap for first string
        hash1= {}
        hash2 = {}

        for char in s:
            if s[char]:
                s[char] += 1
            s[char] = 1

        for char in t:
            if t[char]:
                t[char] += 1
            t[char] = 1

        print(hash1, hash2)

        # 2. Create hashmap for second string
        # 3. Compare hashmap keys and frequencies
        