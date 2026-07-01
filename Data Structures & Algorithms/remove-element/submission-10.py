class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i, n in enumerate(nums):
            if n != val:
                nums[k] = n
                k += 1

        return k