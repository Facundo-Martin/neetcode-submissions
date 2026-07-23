class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = k

        while k < len(nums):
            nums[l], nums[k] = nums[k], nums[l]
            r += 1
            l += 1

        return nums