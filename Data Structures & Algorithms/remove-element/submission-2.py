class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 0. Defensive programming
        indicesToRemove = []
        
        # 1. Iterate over array
        for i, n in enumerate(nums):
            # 2. Find matching vals
            if n == val:
                indicesToRemove.append(i)

        for i, n in enumerate(nums):
            if i in indicesToRemove:
                nums.pop[i]

        return len(nums)
