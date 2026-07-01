class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0


        for i in range(n):
            for j in range(i + 1, n):
                curr_area = (j - i) * min(heights[i], heights[j])
                res = max(res, curr_area)

        return res
        