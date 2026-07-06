class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            height = heights[i]

            # Expand left
            left = i
            while left > 0 and heights[left - 1] >= height:
                left -= 1

            # Expand right
            right = i
            while right < n - 1 and heights[right + 1] >= height:
                right += 1

            width = right - left + 1
            area = height * width

            max_area = max(max_area, area)

        return max_area

       # Brute force approach (traverse array, calculat widths, keep track of area)
       
       
        # Inputs
            # Heights: 1D array, unsorted
            # Type: Int, unsigned
            # Constraints: 0 <= heights[i] <= 1000 and 1 <= heights.length <= 1000
        
        

        # Patterns, invariants, thoughts
            # Invariant 1: Width of rectangle increases by 1 as we traverse array
            # Height of rectangled is determined by shortest bar
            # Since unsorted -> disregard sliding window 7 two pointer techniques

        # Edge cases
            # Return val if arr.len == 1 -> zero? or arr[i]?

        # Outputs
            # Largest area in rectangle -> Int