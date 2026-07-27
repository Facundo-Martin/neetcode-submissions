class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max_heap will store tuples structured as: (-distance, [x, y])
        max_heap = []
        
        for x, y in points:
            dist_squared = (x ** 2) + (y ** 2)
            heapq.heappush(max_heap, (-dist_squared, [x, y]))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # List comprehension to return only the coordinates
        return [point for distance, point in max_heap]