import bisect

class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        # Find position using Binary Search - O(log N)
        # However, underlying list insertion memory shift is still O(N)
        bisect.insort(self.nums, num) 

    def findMedian(self) -> float:
        n = len(self.nums)
        
        # Read from an already sorted array - O(1)
        if n % 2 != 0:
            return float(self.nums[n // 2])
        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0