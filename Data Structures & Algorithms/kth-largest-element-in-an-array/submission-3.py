class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            # Push first k elements directly
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                # Push the new element and immediately pop the smallest
                # if it's larger than the current Kth largest.
                if num > min_heap[0]:
                    heapq.heappushpop(min_heap, num)
                
        # The root of the min-heap is the kth largest element
        return min_heap[0]

    # Inputs:
        # nums: List[int] - An unsorted array of integers.
        # k: int - The target rank (1st largest, 2nd largest, etc.).
        # Edge Case: len(nums) == 1. The loop runs once, returns the single element.

    # Constraints:
        # 1. Duplicates: The array can contain duplicates. The heap naturally handles this.
        # 2. Memory: We only need to store k elements at any time.

    # Algorithm design:
        # State: 
            # Need a data structure to dynamically track the top K elements. 
            # Python's heapq is a min-heap. We push numbers as-is.
            
        # Short circuit / Trimming:
            # We compare the current number to min_heap[0] (the smallest of our top K). 
            # If the current number is smaller, we completely ignore it, skipping heap operations entirely for irrelevant data.
            
        # Array Searching/Sorting strategy:
            # Full Sort (Timsort): O(N log N). Does unnecessary work sorting the entire array.
            # Max-Heap: Would require pushing all N elements (O(N)) and popping K times (O(K log N)).
            # Min-Heap of size K -> [CHOSEN]: Processes in O(N log K) time and O(K) space. Perfect for streams where N is unknown or massive.

    # Outputs:
        # int: The value of the Kth largest element.