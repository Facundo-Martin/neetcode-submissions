class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        ans = []
        n = len(temperatures)

        # Loop through array
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    ans.append(j - i)
                    break
                elif j == n - 1:
                    ans.append(0)

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