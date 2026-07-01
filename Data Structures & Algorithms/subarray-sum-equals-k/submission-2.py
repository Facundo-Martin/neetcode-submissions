class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0
        prefix_sum = { 0: 1}

        for n in nums:
            curr_sum += n

            diff = curr_sum - k
            res += prefix_sum.get(diff, 0)

            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return res