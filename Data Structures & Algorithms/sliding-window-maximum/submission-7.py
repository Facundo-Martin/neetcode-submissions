class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 0. Defensive programming
            # Handle k = nums.len (no need to iterate)
            
        r = 0
        ans = []

        for l in range(len(nums) - k):
            window = nums[l: r]
            window.sort()

            ans.append(window[k])

            r+= 1

        return ans
