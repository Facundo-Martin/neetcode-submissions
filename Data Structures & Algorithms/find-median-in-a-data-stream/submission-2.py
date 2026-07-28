class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num) # Temporarily append to the end - O(1)
        j = len(self.nums) - 2
        
        # Shift elements to the right to create space for the new number - O(N) worst case
        while j >= 0 and self.nums[j] > num:
            self.nums[j + 1] = self.nums[j]
            j -= 1
            
        self.nums[j + 1] = num # Insert at the correct sorted position - O(1)

    def findMedian(self) -> float:
        n = len(self.nums)
        
        # Read from an already sorted array - O(1)
        if n % 2 != 0:
            return float(self.nums[n // 2])
        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0