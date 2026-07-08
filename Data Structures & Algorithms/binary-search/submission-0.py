class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] == target:
                return i

        return -1

        
        # Inputs
            # 1D array, sorted in asc, signed, unique 

        # Constraints:
            # O(logn) time solution -> ??
            # 1 <= nums.length <= 10000
            # -10000 < nums[i], target < 10000


        # Outputs
            # Integer, positive or zero if it exists
            # No solution -> Return -1