class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
            
        # 1. Find the pivot (index of the smallest element)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        pivot = left
        left, right = 0, len(nums) - 1
        
        # 2. Figure out which half to search
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1
            
        # 3. Standard Binary Search on the correct half
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1