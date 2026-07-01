class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Counter with shape of value-frequency -> count = {0: 1, 1: 0, 2: 2}
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue

            new_count = defaultdict(int)

            for n, c in count.items():
                if count[n] > 1:
                    new_count[n] = count[n] - 1
            
            count = new_count

        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)

        return res