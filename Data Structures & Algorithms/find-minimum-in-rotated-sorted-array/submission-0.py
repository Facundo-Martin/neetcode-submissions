class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        for n in nums:
            res = min(res, n)

        return res


        # Inputs
            # nums: 1D array, signed unique int, sorted but rotated.

        # Outputs
            # res: signed integer, minimum element in the array
        
        # Constraints
            # O(log n) solution -> Leaning toward Binary search