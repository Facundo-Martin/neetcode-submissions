class MedianFinder:
    def __init__(self):
        self.small = [] # Max-heap (simulated with negative values)
        self.large = [] # Min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) # Push to max-heap - O(log N)
        
        # Manual boundary check to ensure small max <= large min (from image_fbcd53.jpg)
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]): # Root access - O(1)
            val = -1 * heapq.heappop(self.small)   # Pop from heap - O(log N)
            heapq.heappush(self.large, val)        # Push to heap - O(log N)
            
        # Uneven size checks to balance heaps
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)   # Pop - O(log N)
            heapq.heappush(self.large, val)        # Push - O(log N)
            
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)        # Pop - O(log N)
            heapq.heappush(self.small, -1 * val)   # Push - O(log N)

    def findMedian(self) -> float:
        # Root access based on sizes - O(1)
        if len(self.small) > len(self.large):
            return float(-1 * self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])
            
        return (-1 * self.small[0] + self.large[0]) / 2.0