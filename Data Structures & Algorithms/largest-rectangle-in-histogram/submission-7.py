class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0  # Initialize max area
        n = len(heights)

        # Loop through all possible starting indices
        for i in range(n):
            min_height = float('inf')

            # Loop through all possible ending indices
            for j in range(i, n):
                # Update the minimum height so far
                min_height = min(min_height, heights[j])

                # Calculate area with current width
                width = j - i + 1
                area = min_height * width

                # Update max_area
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