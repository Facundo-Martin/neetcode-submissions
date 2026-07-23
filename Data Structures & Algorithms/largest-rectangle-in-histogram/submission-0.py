class Solution:
    def calculateArea(self, width: int, height: int) -> int:
        return width * height
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = heights[0]
        min_height = heights[0]
        n = len(heights)

        # Handle "edge case"
        if len(heights) == 1:
            return largest_area


        # Brute force approach
        for i in range(n):
            # Invariant!
            width = i + 1

            for j in range(i + 1, n):
                # Keep track of our "trigger" / limiting factor
                min_height = min(min_height, heights[j])

                curr_bar_area = calculateArea(1, heights[j])
                new_total_area = self.calculateArea(width, min_height)

                # Compare all 3 potential solutions!
                largest_area = max(largest_area, new_area, curr_bar_area)

        return largest_area





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