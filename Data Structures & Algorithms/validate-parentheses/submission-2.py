class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        is_valid = True

        pairs = {'(': ')', '{': '}', '[': ']'}

        # Loop through array
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in pairs and s[r] == s[r]:
                is_valid = False
                break
            else:
                l += 1
                r -= 1

        return is_valid







    # Inputs
    # 1. String
        # Type: Only '(', ')', '{', '}', '[' and ']'.
        # 1 <= s.length <= 10^3


    # Constraints & Patterns
        # 1 <= s.length <= 1000 -> O(n^2) would work -> We will still aim for O(n)
        # Only valid if closing pair in order

    # Keywords -> None
    
    # Edge cases
        # 1. If len(s) == 1 -> We know it's invalid -> No chance for a pair
        # 2. If len(s) is uneven -> No pair -> We know it's invalid

    # Outputs
        # Boolean -> True if is_valid, else false