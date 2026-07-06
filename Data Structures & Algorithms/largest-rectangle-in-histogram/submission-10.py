class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        prev_smaller = [-1] * n
        next_smaller = [n] * n

        stack = []

        # Previous Smaller
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                prev_smaller[i] = stack[-1]

            stack.append(i)

        stack.clear()

        # Next Smaller
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                next_smaller[i] = stack[-1]

            stack.append(i)

        max_area = 0

        for i in range(n):
            width = next_smaller[i] - prev_smaller[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area