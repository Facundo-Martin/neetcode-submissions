class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        # As long as there is at least one completed pair sitting side-by-side...
        while "()" in s or "[]" in s or "{}" in s:
            # Erase them by replacing them with empty space!
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        
        # If we successfully cleared out the whole string, it's valid.
        # If anything is left over (like "(]" or "[(])"), it's invalid.
        return s == ""







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