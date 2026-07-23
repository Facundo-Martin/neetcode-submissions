class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []

        for num, idx in enumerate(nums):
            for num2, idx2 in enumerate(nums):
                if idx == idx2 or num == num2:
                    continue
                if num + num2 == target:
                    indexes.append(idx, idx2)
                else:
                    continue

        return indexes
