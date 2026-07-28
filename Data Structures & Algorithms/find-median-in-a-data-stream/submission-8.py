from heapq import heappush, heappop, heappushpop

class MedianFinder:
    def __init__(self):
        self.large = []  # Min-heap
        self.small = []  # Max-heap (simulated with negatives)

    def addNum(self, num: int) -> None:
        # Pass through small heap to guarantee the correct element goes to large heap
        # heappushpop is highly optimized - O(log N) combined operation
        heappush(self.large, -heappushpop(self.small, -num))
        
        # Balance condition: enforce that small heap always holds the extra element - O(log N)
        if len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        # If total elements is odd, small heap holds the median - O(1)
        if len(self.small) > len(self.large):
            return float(-self.small[0])
            
        # If total elements is even, average the roots - O(1)
        return (-self.small[0] + self.large[0]) / 2.0