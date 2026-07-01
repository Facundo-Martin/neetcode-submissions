class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(nums)

        # Iterate to fix the first two elements
        for i in range(n):
            for j in range (i + 1, n):
                # Keep track of visited elements in third loop
                seen = set()

                # Loop to fix the third element and find the fourth
                for k in range (j + 1, n):
                    # Need to find the remaining one
                    three_sum = nums[i] + nums[j] + nums[k]
                    last = target - three_sum

                    if last in seen:
                        curr = [nums[i], nums[j], nums[k], last]
                        curr.sort()
                        res.add(tuple(curr))

                    # Add current number to the set for future lookup
                    else: 
                        seen.add(nums[k])

        return [list(t) for t in res]