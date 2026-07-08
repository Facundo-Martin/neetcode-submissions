class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
                
            # Check if the left sorted portion exists
            if nums[low] <= nums[mid]:
                # Is the target inside this left sorted portion?
                if nums[low] <= target < nums[mid]:
                    high = mid - 1 # Search left
                else:
                    low = mid + 1  # Search right
            
            # Otherwise, the right portion must be sorted
            else:
                # Is the target inside this right sorted portion?
                if nums[mid] < target <= nums[high]:
                    low = mid + 1  # Search right
                else:
                    high = mid - 1 # Search left
                    
        return -1