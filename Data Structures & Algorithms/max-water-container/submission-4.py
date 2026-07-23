class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights - 1)

        while l < r:
            curr_area = (r - l) * min(heights[l], heights[r])
            res = max(res, curr_area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return res
        