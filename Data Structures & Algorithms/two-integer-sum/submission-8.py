class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            for idx2, num2 in enumerate(nums[idx + 1:], start=idx + 1):
                if num + num2 == target:
                    return [idx, idx2]