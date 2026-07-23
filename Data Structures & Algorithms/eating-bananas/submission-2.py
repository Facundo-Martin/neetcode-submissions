class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        
        while True:
            eating_hours = 0
            
            for pile in piles:
                # Instead of a while loop, use integer division to find the hours.
                # (pile + k - 1) // k is the formula for rounding up integer division.
                # e.g., pile = 7, k = 3 -> (7 + 3 - 1) // 3 = 9 // 3 = 3 hours.
                eating_hours += (pile + k - 1) // k
            
            if eating_hours <= h:
                return k
                
            k += 1



        # Inputs
            # Piles: 1D array, signed int, sorted or unsorted?
            # h: unsigned int

        # Outputs
            # Min eating rate

        # Constraints
            # k: bananas-per-hour eating rate
            # If pile.len < k, can't hop to another pile
            # Edge case: If h == arr.len -> k has to be the size of the largest element