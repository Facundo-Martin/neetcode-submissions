class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num) # Append to end - O(1)

    def findMedian(self) -> float:
        self.nums.sort() # Sort array using Timsort - O(N log N)
        n = len(self.nums)
        
        if n % 2 == 1:
            return float(self.nums[n // 2]) # Array access - O(1)
            
        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0 # Array access - O(1)