class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. Construct hashmap
        # 2. Return hashmap length === nums.len
        deduped = set(nums)
        return deduped.len() != nums.len

        