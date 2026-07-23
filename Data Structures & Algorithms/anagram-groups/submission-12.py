class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {} # Dic of type []:[]

        for s in strs:
            group = [0] * 26 # String represented in alphabet-sized (a-z) array

            for c in s:
                group[ord(c) - ord('a')] += 1

            key = tuple(group)
            if key in ans:
                ans[key].append(s)
            ans[key] = [s]

        return list(ans.values())