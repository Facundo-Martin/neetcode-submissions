import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        
        # Pick a random pivot
        pivot = random.choice(nums)
        
        # Partitioning into three new lists (Descending order concept)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        # If k falls within the 'left' partition, recurse left
        if k <= L:
            return self.findKthLargest(left, k)
            
        # If k falls within the 'right' partition, recurse right
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
            
        # Otherwise, the kth element is one of our pivot duplicates
        else:
            return mid[0]

    # Inputs:
        # nums: List[int] - An unsorted array of integers.
        # k: int - The target rank (1st largest, 2nd largest, etc.).
        # Edge Case: nums is empty (returns immediately).

    # Constraints:
        # 1. Duplicates: Elegantly handles massive amounts of duplicates by grouping them all in the 'mid' array.
        # 2. Memory: Uses O(N) auxiliary space per recursive call to instantiate the new left, mid, and right arrays.

    # Algorithm design:
        # State: 
            # Separates the current array into three completely new arrays representing elements greater than, equal to, and less than the pivot.
            
        # Short circuit / Trimming:
            # Determines exactly which of the three arrays contains the Kth largest element. It recurses ONLY on that specific array, completely discarding the other two from memory and future processing.
            
        # Array Searching/Sorting strategy:
            # QuickSelect (Pythonic 3-Way) -> [CHOSEN]: Achieves average O(N) time. Maximizes readability and completely avoids pointer/index math during interviews, but sacrifices memory efficiency (O(N) space) compared to the in-place version.

    # Outputs:
        # int: The value of the Kth largest element.