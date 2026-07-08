class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0]) # Safe since 1 <= m, n <= 100

        # Scan first row
        for i in range(n):
            # Get every element of row
            for j in range(m):
                if matrix[i][j] == target:
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