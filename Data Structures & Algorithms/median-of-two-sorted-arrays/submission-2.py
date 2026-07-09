class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr = sorted(nums1 + nums2)
        length = len(arr)
        
        mid = length // 2
        
        if length % 2 == 0:
            # Even: Average of the two middle elements
            return (arr[mid - 1] + arr[mid]) / 2.0
        else:
            # Odd: The middle element
            return float(arr[mid])


        # Inputs:
            # 1D arrays, sorted, signed, -10^6 <= nums1[i], nums2[i] <= 10^6
            # 0 <= m <= 1000 -> What happens if both are zero?
            # Are the values unique??



        # Output:
            # median: float, signed, in theory -10^6 <= median <= 10^6
            # What happens on no return? 