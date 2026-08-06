class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        state = []
        
        # Standard stack validation for parentheses
        def is_valid(path):
            stack = []
            for char in path:
                if char == "(":
                    stack.append(char)
                else: # char is ")"
                    if not stack:
                        return False
                    stack.pop()
            return len(stack) == 0

        def backtrack(path):
            # Base case: string is complete
            if len(path) == n * 2:
                # Only append if the stack validation passes
                if is_valid(path):
                    res.append("".join(path))
                return
            
            # Blindly explore all combinations (2 branches every time)
            for choice in ["(", ")"]:
                path.append(choice)
                backtrack(path)
                path.pop()

        backtrack([])
        
        return res