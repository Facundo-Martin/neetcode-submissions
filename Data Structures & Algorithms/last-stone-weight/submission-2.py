class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        # Space: O(N) to store the new list in memory.
        # Time: O(N) to iterate through all N stones and invert them.
        max_heap = [-s for s in stones]
        
        # Time: O(N) to arrange the list into a valid heap structure.
        # (Fun fact: heapify is extremely optimized and runs in linear time!)
        heapq.heapify(max_heap)
        
        # The loop runs at most N times (we remove at least 1 stone per turn)
        while len(max_heap) > 1:
            
            # Time: O(log N) to remove the root and fix the tree structure.
            first = heapq.heappop(max_heap)
            
            # Time: O(log N) to remove the new root and fix the tree structure.
            second = heapq.heappop(max_heap)
            
            if first != second:
                # Time: O(log N) to add the new weight and bubble it up to its proper place.
                heapq.heappush(max_heap, first - second)
                
        # Time: O(1) to just look at the first item in the array.
        return -max_heap[0] if max_heap else 0