class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 0. Defensive programming
            # Handle k = nums.len (no need to iterate)
            
        r = k
        ans = []

        for l in range(len(nums) - k):
            window = nums[l: r]
            window.sort()

            ans.append(window[-1])

            r+= 1

        return ans
