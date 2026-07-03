class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        ans = [0] * n 
        stack = [] 

        for i in range(n):
            current_temp = temperatures[i]

            # Resolve past days: 
            while stack and current_temp > temperatures[stack[-1]]:
                # Today resolves the day at the top of the stack
                prev_day_index = stack.pop()
                # Calculate the distance and record it
                ans[prev_day_index] = i - prev_day_index
            
            # After resolving any older colder days, today now enters the waiting room
            stack.append(i)

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