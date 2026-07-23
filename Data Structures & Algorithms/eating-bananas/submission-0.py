class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        eating_hours = 0

        while eating_hours > h:
            for pile in piles:
                remaining = pile
                while remaining > 0:
                    remaining -= k
                    eating_hours += 1
                if eating_hours > h:
                    k += 1
                    break
        return k



        # Inputs
            # Piles: 1D array, signed int, sorted or unsorted?
            # h: unsigned int

        # Outputs
            # Min eating rate

        # Constraints
            # k: bananas-per-hour eating rate
            # If pile.len < k, can't hop to another pile
            # Edge case: If h == arr.len -> k has to be the size of the largest element