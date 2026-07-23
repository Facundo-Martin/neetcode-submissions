class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        closing_pairs = {
        ")": "(", 
        "}": "{" , 
        "]": "[" }

        for char in s:
            # Handle closing parenthesis
            if char in closing_pairs:
                # Check if most recent value is pair and rm
                if stack and stack[-1] == closing_pair[char]:
                    stack.pop()
                else:
                    return False
            # Handle opening parentheses
            else:
                stack.append(char)

        return len(stack) == 0
                







    # Inputs
    # 1. String
        # Type: Only '(', ')', '{', '}', '[' and ']'.
        # 1 <= s.length <= 10^3


    # Constraints & Patterns
        # 1 <= s.length <= 1000 -> O(n^2) would work -> We will still aim for O(n)
        # Only valid if closing pair in order -> We need to start with opening parentheses!

    # Keywords -> None
    
    # Edge cases
        # 1. If len(s) == 1 -> We know it's invalid -> No chance for a pair
        # 2. If len(s) is uneven -> No pair -> We know it's invalid

    # Outputs
        # Boolean -> True if is_valid, else false