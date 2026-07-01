class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(nums)

        # Fix 3 values, see if we can find the 4th one in the set
        for i in range(n):
            for j in range (i + 1, n):
                seen = set()

                for k in range (j + 1, n):
                    # Need to find the remaining one
                    missing = target - (nums[i] + nums[j] + nums[k])

                    if missing in seen:
                        curr = [nums[i], nums[j], nums[k], missing]
                        curr.sort()
                        res.add(tuple(curr))

                    # If we can't find missing number, add current number to set
                    else: 
                        seen.add(nums[k])

        return [list(t) for t in res]