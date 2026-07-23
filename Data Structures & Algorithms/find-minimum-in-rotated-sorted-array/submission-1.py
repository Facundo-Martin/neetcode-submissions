def findMinOptimized(nums: List[int]) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1
    
    while l <= r:
        # If the current window is already completely sorted, 
        # the leftmost element is the minimum of this window.
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
            
        m = (l + r) // 2
        res = min(res, nums[m])
        
        # Decide which half to throw away
        if nums[m] >= nums[l]:
            # Mid is in the left sorted portion, meaning the min is to our right
            l = m + 1
        else:
            # Mid is in the right sorted portion, min is to our left
            r = m - 1
            
    return res

        # Inputs
            # nums: 1D array, signed unique int, sorted but rotated.

        # Outputs
            # res: signed integer, minimum element in the array
        
        # Constraints
            # O(log n) solution -> Leaning toward Binary search