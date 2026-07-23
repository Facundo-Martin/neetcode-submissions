class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1  # Start with the minimum possible eating speed
        
        while True:
            eating_hours = 0
            
            for pile in piles:
                # math.ceil(pile / k) calculates how many hours this pile takes.
                # e.g., pile = 7, k = 3 -> ceil(7/3) = 3 hours.
                eating_hours += math.ceil(pile / k)
            
            # If total hours spent is within the guardrail 'h', we found our minimum k!
            if eating_hours <= h:
                return k
            
            # Otherwise, Koko ate too slowly. Reset and try the next speed.
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