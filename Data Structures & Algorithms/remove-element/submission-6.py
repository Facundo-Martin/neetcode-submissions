class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.remove(val)
        print(nums)
        return len(nums)
