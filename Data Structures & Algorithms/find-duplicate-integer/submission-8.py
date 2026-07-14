class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # The possible range of numbers is [1, n]
        low, high = 1, len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            # Count how many elements are <= mid

            # Count how many numbers in the array are less than or equal to 'mid'
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            # By the Pigeonhole Principle:
            # If the count of numbers <= mid is greater than mid itself,
            # it means the duplicate must be in the lower half [low, mid].
            if count > mid:
                high = mid
            # Otherwise, the duplicate must be in the upper half [mid + 1, high].
            else:
                low = mid + 1
        
        # At the end of the loop, low and high will meet at the duplicate number
        return low
        