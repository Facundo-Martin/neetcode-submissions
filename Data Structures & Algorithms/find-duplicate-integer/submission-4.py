class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Finding the intersection point in the cycle
        tortoise = nums[0]
        hare = nums[0]
        
        # Move once to start the loop
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            
        # Phase 2: Finding the entrance to the cycle (the duplicate)
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        return tortoise
        