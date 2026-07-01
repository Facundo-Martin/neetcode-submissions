class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # Points to the last valid element in nums1
        j = n - 1 # Points to the last element in nums2
        k = m + n - 1 # Points to the last position in the merged array (end of nums1)

        # Execute loop until there are no more elements in nums2 to copy over
        while j >= 0:
            # Make sure i is in bound first
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
