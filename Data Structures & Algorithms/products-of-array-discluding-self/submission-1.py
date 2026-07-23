class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i, n in enumerate(nums):
            res[i] = prefix
            prefix *= n
        
        postfix = 1 
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= num[i]
        
        return res