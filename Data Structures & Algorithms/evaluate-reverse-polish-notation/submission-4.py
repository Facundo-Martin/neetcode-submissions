class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        operators = {"+", "-", "*", "/"}

        for c in tokens:
            # Handle operators
            if c not in operators:
                stack.append(int(c))
           
            else:
                operator = c
                last, first = stack.pop(), stack.pop()

                if operator == "+":
                    stack.append(first + last)
                if operator == "-":
                    stack.append(first - last)
                if operator == "*":
                    stack.append(first * last)
                if operator == "/":
                    stack.append(int(first / last))

        return stack.pop()

        # Inputs
            # tokens:
                # DS: Array
                # Data Type: string -> "+", "-", "*", or "/" or -200 <= int <= 200
                # Structure type: unsorted

        # Constraints & Edge Cases
            # 1 <= tokens.length <= 1000
            # tokens[i] is "+", "-", "*", or "/" or -200 <= int <= 200 
                # Edge case: Dealing with arithmetic while extracting string values! -> Parse


        # Keywords & Patterns
            # 1 <= tokens.length <= 10^3 -> O(n^2) will work (not timeout)
                # Still aiming for single pass on array (O(n)) + linear time computation O(1)
            # "valid arithmetic expression" -> Show LIFO pattern -> Leaning toward a stack


        # Outputs
            # Evaluation of the expression
                # Data type: Integer
                # constraints? -> None

