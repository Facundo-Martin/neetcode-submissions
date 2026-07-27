import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            # Use negative distance to simulate a max-heap (largest distance becomes smallest number)
            dist = -(x**2 + y**2)
            
            # Maintain exactly k elements in the heap
            if len(max_heap) == k:
                heapq.heappushpop(max_heap, (dist, x, y))
            else:
                heapq.heappush(max_heap, (dist, x, y))
                
        # Extract and return only the coordinates
        return [[x, y] for dist, x, y in max_heap]

    # Inputs:
        # points: List[List[int]] - An array of [x, y] coordinate pairs.
        # k: int - The number of closest points we need to return.
        # Edge Case: k == len(points). Return the original list immediately.

    # Constraints:
        # 1. Distance: Calculated via Euclidean distance. Since we only compare relative sizes, x^2 + y^2 is sufficient (omit sqrt for performance).
        # 2. Priority: We need to efficiently track the K minimum distances out of N total points.
        # 3. Order: The exact order of the returned k points does NOT matter.

    # Algorithm design:
        # Edge cases:
            # if k == len(points): return points (no sorting needed).
        
        # State: 
            # Need a data structure that dynamically keeps the K smallest elements.
            # Python's heapq is a min-heap by default. We must invert distances (multiply by -1) to simulate a max-heap.
            
        # Short circuit / Trimming:
            # By using heappushpop when the heap size reaches K, we immediately discard the new point if it's further away than our current worst point, avoiding unnecessary tree traversals.
        
        # Array Searching/Sorting strategy:
            # Full Sort (Timsort): Poor fit. O(N log N). Does unnecessary work sorting the remaining N-K elements.
            # Quickselect: Great fit for in-memory arrays. O(N) average time, but worst-case is O(N^2) and it cannot handle live streaming data.
            # Max-Heap -> [CHOSEN]: Best all-around fit. Guaranteed O(N log K) time, O(K) extra space. Safely handles massive datasets or live streams because memory never exceeds size K.

    # Outputs:
        # List[List[int]]: The K coordinate pairs that are closest to the origin.