class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0]) if num_rows > 0 else 0
        
        # 1. Binary search to find the correct row
        top = 0
        bot = num_rows - 1
        
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
                
        if not (top <= bot):
            return False
            
        # 2. Classic binary search within the identified row
        target_row = (top + bot) // 2
        l = 0
        r = num_cols - 1
        
        while l <= r:
            m = (l + r) // 2
            if target > matrix[target_row][m]:
                l = m + 1
            elif target < matrix[target_row][m]:
                r = m - 1
            else:
                return True
                
        return False


        # Inputs
            # Array, 2D, sorted in ascending, int type, signed
            # Ascending within a row and all around rows

        # Outputs
            # Bool -> True if it exists, false otherwise

        # Constraints
            # O(log(m * n)) time solution -> Leaning into ??
            # m == matrix.length
            # n == matrix[i].length
            # 1 <= m, n <= 100
            # -10000 <= matrix[i][j], target <= 10000