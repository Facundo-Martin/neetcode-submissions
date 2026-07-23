class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The absolute maximum speed Koko ever needs is the size of the largest pile.
        max_speed = max(piles)
        
        # Linearly test every speed from 1 up to the maximum speed
        for speed in range(1, max_speed + 1):
            total_hours = 0
            
            for pile in piles:
                # Efficiently calculate ceiling division without math.ceil()
                total_hours += (pile + speed - 1) // speed
            
            # The moment we find a speed that works, return it immediately
            if total_hours <= h:
                return speed
                
        return max_speed



        # Inputs
            # Piles: 1D array, signed int, sorted or unsorted?
            # h: unsigned int

        # Outputs
            # Min eating rate

        # Constraints
            # k: bananas-per-hour eating rate
            # If pile.len < k, can't hop to another pile
            # Edge case: If h == arr.len -> k has to be the size of the largest element