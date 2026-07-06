class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        leftsmall = [0] * n
        rightsmall = [0] * n

        # Compute NSL (Nearest Smaller to Left)
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            leftsmall[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)

        # Clear the stack
        stack.clear()

        # Compute NSR (Nearest Smaller to Right)
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            rightsmall[i] = n - 1 if not stack else stack[-1] - 1
            stack.append(i)

        # Calculate max area
        max_area = 0
        for i in range(n):
            width = rightsmall[i] - leftsmall[i] + 1
            max_area = max(max_area, heights[i] * width)

        return max_area