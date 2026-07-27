class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Sorts in-place from largest to smallest
        nums.sort(reverse=True) 
        
        # 1st largest is at index 0, 2nd at index 1, so kth is at k - 1
        return nums[k - 1]

    # Inputs:
        # nums: List[int] - An unsorted array of integers.
        # k: int - The target rank (1st largest, 2nd largest, etc.).
        # Edge Case: k == len(nums). Returns nums[0], which correctly yields the smallest element.

    # Constraints:
        # 1. Mutability: nums.sort() sorts the array in-place. If the input array must remain unchanged, you must use sorted(nums) which strictly requires O(N) space to create a new list.
        # 2. Over-processing: This forces the computer to completely order all N elements, even though we only care about a single element's position.

    # Algorithm design:
        # State: 
            # The entire array is sorted using Python's built-in Timsort algorithm (a hybrid of merge sort and insertion sort).
            
        # Short circuit / Trimming:
            # None. This algorithm does not stop early. It does the full work of sorting every element regardless of the value of K.
            
        # Array Searching/Sorting strategy:
            # Full Sort -> [CHOSEN]: Runs in O(N log N) time and up to O(N) space. 
            # While it is practically fast for small to medium datasets due to C-level optimizations, it fails scalability tests when N is massive (e.g., billions of rows in a database) or when the data is streaming in real-time.

    # Outputs:
        # int: The value of the Kth largest element.