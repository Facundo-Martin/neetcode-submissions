class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to max heap by negating values (Python only has min heap)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
      
        # Keep smashing stones until at most one remains
        while len(max_heap) > 1:
            # Extract two heaviest stones (negate to get original values)
            first_stone = -heapq.heappop(max_heap)
            second_stone = -heapq.heappop(max_heap)
          
            # If stones have different weights, push the difference back
            if first_stone != second_stone:
                # Push negative of difference to maintain max heap property
                heapq.heappush(max_heap, -(first_stone - second_stone))
      
        # Return 0 if no stones left, otherwise return the last stone's weight
        return 0 if not max_heap else -max_heap[0]

        

