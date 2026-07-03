class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
        
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