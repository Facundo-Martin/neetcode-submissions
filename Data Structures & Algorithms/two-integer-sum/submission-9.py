class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # value-index key pair

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [i, hasmap[diff]]
            else: 
                hasmap[n] = i