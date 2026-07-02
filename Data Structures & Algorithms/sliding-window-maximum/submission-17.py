class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0:
            return []
            
        # dq will store indices of useful elements in every window
        dq = deque()
        result = []
        
        # Process first window of size k
        for i in range(k):
            # Remove elements from rear that are smaller than the current element
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            
        # Process rest of the elements
        for i in range(k, n):
            # Front element of dq is the largest element of the previous window
            result.append(nums[dq[0]])
            
            # Out of Bounds check: Remove front element if it slid out of window
            while dq and dq[0] <= i - k:
                dq.popleft()
                
            # Monotonic property: clear out smaller elements from rear
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
                
            dq.append(i)
            
        # Append the maximum element of the last window
        result.append(nums[dq[0]])
        return result
