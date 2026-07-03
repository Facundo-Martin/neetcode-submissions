class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n 

        for i in range(n):
            for j in range(i + 1, n):
                # Overwrite the 0 with the actual distance if valid
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i  
                    break      

        return ans

        
        # Inputs
            # Type: Array 1D
            # Data type: int
            # Structure: unsorted


        # Constraints
            # 1 <= temperatures.length <= 10^3 
                # -> O(n^2) won't time out
                # -> Aim for O(n) time with single pass on array
            # 1 <= temperatures[i] <= 100

        # Edge cases -> None

        # Patterns
            # 1. We care about comparing values
            # 2. We care about latter_temp > former_temp

        # Outputs
            # Type: Array 1D
            # Data type: int
            # Edge cases: No warmer day -> Arr[i] == 0