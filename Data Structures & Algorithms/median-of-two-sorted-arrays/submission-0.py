class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if not nums1 and not nums2:
            return 0.0

        arr = nums1 + nums2
        arr.sort()

        if len(arr) // 2 == 0:
            m = len(arr) // 2
            return arr[m]
        else:
            m1 = math.floor(len(arr) / 2)
            m2 = math.ceil(len(arr) / 2)
            return (arr[m1] + arr[m2]) / 2


        # Inputs:
            # 1D arrays, sorted, signed, -10^6 <= nums1[i], nums2[i] <= 10^6
            # 0 <= m <= 1000 -> What happens if both are zero?
            # Are the values unique??



        # Output:
            # median: float, signed, in theory -10^6 <= median <= 10^6
            # What happens on no return? 