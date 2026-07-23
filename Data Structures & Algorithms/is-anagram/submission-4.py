class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 0. Defensive programming
        # 1. Create hashmap for first string
        hash1= {}
        hash2 = {}

        for char in s:
            if hash1[char]:
                hash1[char] += 1
            hash1[char] = 1

        for char in t:
            if hash2[char]:
                hash2[char] += 1
            hash2[char] = 1

        print(hash1, hash2)

        # 2. Create hashmap for second string
        # 3. Compare hashmap keys and frequencies
        