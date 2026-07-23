class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 0. Defensive programming (pointer out of bounds)
        # 1. Data structures (identify, choose, init)
        # 2. Data handling (code block, etc)
        # 3. Data manipulation (return statements, etc)

        # 1. 
        i, j = m, 0 

        while i < len(nums1) and j < len(nums2):
            nums1[i] = nums2[j]
            i += 1
            j += 1

        