class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        # The loop stops when l == r, pinpointing the minimum element
        while l < r:
            m = (l + r) // 2
        
            # If the middle element is greater than the rightmost element,
            # the inflection point (and minimum) must be in the right half.
            if nums[m] > nums[r]:
                l = m + 1
            # Otherwise, the minimum is at 'm' or somewhere to its left.
            else:
                r = m

        return nums[l]

        # Inputs
            # nums: 1D array, signed unique int, sorted but rotated.

        # Outputs
            # res: signed integer, minimum element in the array
        
        # Constraints
            # O(log n) solution -> Leaning toward Binary search