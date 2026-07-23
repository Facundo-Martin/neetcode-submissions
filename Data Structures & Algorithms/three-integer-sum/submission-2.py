class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            # Avoid duplicate values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Init left and right pointers for 2sum
            l, r = i + 1, n - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                # Sum too large -> Decrease pointer
                if three_sum > 0:
                    r -= 1

                # Sum too small -> Increase pointer
                elif three_sum < 0:
                    l += 1

                # sum == 0, found our triplets
                else:
                    res.append(nums[i], nums[l], nums[r])

                    # Increase pointer, but it could be the same num as the previous one!
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
        