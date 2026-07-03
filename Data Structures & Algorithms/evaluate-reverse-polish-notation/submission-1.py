class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        operators = {"+", "-", "*", "/"}

        # Keep scanning and collapsing until only 1 element is left
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in operators:
                    # Found an operator! Extract the two preceding operands
                    op1 = int(tokens[i - 2])
                    op2 = int(tokens[i - 1])
                    operator = tokens[i]
                    
                    # Perform the calculation with truncation toward zero
                    if operator == "+":
                        res = op1 + op2
                    elif operator == "-":
                        res = op1 - op2
                    elif operator == "*":
                        res = op1 * op2
                    elif operator == "/":
                        # int() handles truncation toward zero automatically for floats
                        res = int(op1 / op2)
                    
                    # Collapse the array:
                    # 1. Replace the first operand with the result
                    tokens[i - 2] = str(res)
                    
                    # 2. Delete the second operand and the operator
                    # Note: Deleting index i-1 first preserves the relative position of index i
                    del tokens[i]
                    del tokens[i - 1]
                    
                    # Break out of the inner loop to restart the scan from index 0
                    break
                    
        return int(tokens[0])

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

