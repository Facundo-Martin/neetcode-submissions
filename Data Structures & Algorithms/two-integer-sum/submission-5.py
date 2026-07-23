class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []

        for idx, num in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if idx == idx2 or num == num2:
                    continue
                if num + num2 == target:
                    indexes.extend([idx, idx2])
                    break
                else:
                    continue

        return indexes
