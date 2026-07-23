class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []

        for id, str in enumerate(strs):
            target = strs[0][id] # grab character from first str

            if str == target:
                if id == len(strs) - 1:
                    ans.append(target)
                else:
                    continue
            else:
                break

        return ans

