class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(path, open_count, closed_count):
            # Base case: string is complete (and guaranteed valid)
            if len(path) == n * 2:
                res.append("".join(path))
                return
            
            # Option 1: Add an open bracket 
            # Valid as long as we haven't used all 'n' open brackets
            if open_count < n:
                path.append("(")
                backtrack(path, open_count + 1, closed_count)
                path.pop()
                
            # Option 2: Add a closed bracket 
            # Valid as long as there are unmatched open brackets to close
            if closed_count < open_count:
                path.append(")")
                backtrack(path, open_count, closed_count + 1)
                path.pop()

        # Start with an empty path, 0 open, and 0 closed brackets
        backtrack([], 0, 0)
        
        return res