class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Step 1: Define boundaries
        l, r = 1, max(piles)
        res = r # Default to worst-case maximum speed
        
        # Step 3: Binary Search on the sorted range
        while l <= r:
            k = (l + r) // 2
            
            # Step 2: Test feasibility of speed 'k'
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            # Step 3 (Continued): Shift boundaries based on test
            if hours <= h:
                res = k      # 'k' works, record it!
                r = k - 1    # Can we go even slower? Search left.
            else:
                l = k + 1    # Too slow! Search right.
                
        return res


        # Inputs
            # Piles: 1D array, signed int, sorted or unsorted?
            # h: unsigned int

        # Outputs
            # Min eating rate

        # Constraints
            # k: bananas-per-hour eating rate
            # If pile.len < k, can't hop to another pile
            # Edge case: If h == arr.len -> k has to be the size of the largest element