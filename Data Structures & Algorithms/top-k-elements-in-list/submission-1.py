class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        ans = []

        for n in nums:
            count[n] += 1
        
        for key, value in count.items():
            if value >= k:
                ans.append(key)

        return ans


        