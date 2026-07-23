class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 0. Defensive programming
            # Handle k = nums.len (no need to iterate)
            
        l, r = 0, k
        ans = []

        while r <= len(nums) - k:
            window = nums[l: r]
            window.sort()

            ans.append(window[-1])

            r += 1
            l += 1
        
        return ans
