class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        while k <= len(nums):
            nums[l], nums[k] = nums[k], nums[l]
            k += 1

        return nums