class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        for idx, num in enumerate(nums):
            if num == nums[idx + 1]:
                return num
        