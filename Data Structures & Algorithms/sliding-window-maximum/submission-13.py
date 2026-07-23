class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        # Loop for each window position
        for i in range(n - k + 1):
            current_max = arr[i]
            
            # Scan the current window of size k
            for j in range(1, k):
                if arr[i + j] > current_max:
                    current_max = arr[i + j]
            result.append(current_max)

        return result
