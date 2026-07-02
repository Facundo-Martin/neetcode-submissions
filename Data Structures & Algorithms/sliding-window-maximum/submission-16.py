class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0:
            return []
            
        # Store elements as (-value, index) because Python heapq is a min-heap
        heap = []
        result = []
        
        # Initialize the first window
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        result.append(-heap[0][0])
        
        # Process the remaining elements
        for i in range(k, n):
            heapq.heappush(heap, (-nums[i], i))
            
            # Lazy Deletion: Remove elements from the top if they are out of bounds
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
                
            result.append(-heap[0][0])
            
        return result
