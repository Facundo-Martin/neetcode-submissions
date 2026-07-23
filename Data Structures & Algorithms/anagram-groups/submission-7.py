class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) # Dic of type []:[]

        for s in strs:
            group = [0] * 26 # String represented in alphabet-sized (a-z) array

            for c in s:
                group[ord(c) - ord('a')] += 1
                # Note: How do we get the index?

            ans[tuple(group)].append(s)
            # Note: What happens if this does not exist?
            
        return ans.values()
        