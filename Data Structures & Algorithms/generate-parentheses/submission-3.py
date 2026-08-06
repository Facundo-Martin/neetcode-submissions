class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = []
        
        def backtrack(open_count, closed_count):
            # Base case: string is complete
            if len(path) == n * 2:
                res.append("".join(path))
                return
            
            # Option 1: Add an open bracket 
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, closed_count)
                path.pop()
                
            # Option 2: Add a closed bracket 
            if closed_count < open_count:
                path.append(")")
                backtrack(open_count, closed_count + 1)
                path.pop()

        # Start with 0 open and 0 closed brackets
        backtrack(0, 0)
        
        return res