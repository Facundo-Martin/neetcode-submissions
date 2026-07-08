class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        # Virtual 1D array boundaries
        total_elements = num_rows * num_cols
        l = 0
        r = total_elements - 1
 
        while l <= r:
            mid = (l + r) // 2
            
            # Map the 1D index back to 2D coordinates
            row = mid // num_cols
            col = mid % num_cols
            mid_num = matrix[row][col]
 
            if target == mid_num:
                return True
            elif target < mid_num:
                r = mid - 1
            else:
                l = mid + 1
 
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