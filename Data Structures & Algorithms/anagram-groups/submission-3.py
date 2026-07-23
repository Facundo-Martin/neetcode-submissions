class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        for i, s1 in enumerate(strs):
            group = [s1]
            for j, s2 in enumerate(strs[i+1:], start= i+1):
                if len(s1) != len (s2):
                    continue
                if sorted(s1) == sorted(s2):
                    group.append(s2)
                if j == len(strs) - 1:
                    ans.append(group)


        return ans
        