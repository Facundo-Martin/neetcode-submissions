class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
                
            # Check if the left sorted portion exists
            if nums[l] <= nums[mid]:
                # Is the target inside this left sorted portion?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1 # Search left
                else:
                    l = mid + 1  # Search right
            
            # Otherwise, the right portion must be sorted
            else:
                # Is the target inside this right sorted portion?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Search right
                else:
                    r = mid - 1 # Search left
                    
        return -1