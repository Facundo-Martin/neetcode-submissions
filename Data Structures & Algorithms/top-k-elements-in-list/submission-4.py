class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = defaultdict(int)
        freq_buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        for num, freq in count.items():
            freq_buckets[freq].append(num)

        for i in range(len(freq_buckets) - 1, 0, -1):
            for n in freq_buckets[i]:
                ans.append(n)
                if len(res) >= k:
                   break

        return ans


        