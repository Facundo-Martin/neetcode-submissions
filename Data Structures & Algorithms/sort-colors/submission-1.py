class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, l, r = 0, 0, len(nums) - 1

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        while i <= r:
            if nums[i] == 0: # Swap left pointer with i pointer value
                swap(i, l)
                l += 1

            elif nums[i] == 2:
                 swap(i, r)
                 r += 1
                 r -= 1

            i += 1