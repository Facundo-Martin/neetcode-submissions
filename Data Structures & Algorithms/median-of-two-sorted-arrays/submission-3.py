class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to minimize the binary search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        l, r = 0, m

        # Target length for the left half (median position if arrays were merged).
        # The +1 ensures the left half gets the extra element when the total length is odd.
        total_len = m + n
        half_len = (total_len + 1) // 2

        while l <= r:
            i = (l + r) // 2 # Cut point for nums1
            j = half_len - i  # Cut point from nums2
            
            # nums1 boundaries around cut i
            l1 = nums1[i - 1] if i > 0 else float('-inf')
            r1 = nums1[i] if i < m else float('inf')
            
            # nums2 boundaries around cut j
            l2 = nums2[j - 1] if j > 0 else float('-inf')
            r2 = nums2[j] if j < n else float('inf')

            # Did we find the perfectly balanced cut?
            if l1 <= r2 and l2 <= r1:
                # If total length is odd, median is the biggest number on the left
                if (m + n) % 2:
                    return float(max(l1, l2))
                # If even, median is average of left max and right min
                return (max(l1, l2) + min(r1, r2)) / 2.0
            
            # l1 > r2 means our cut is too far right. 
            # r = i - 1 instantly eliminates the entire right half of the search space.
            elif l1 > r2:
                r = i - 1
                
            # Otherwise, our cut is too far left. 
            # l = i + 1 instantly eliminates the entire left half of the search space.
            else:
                l = i + 1


        # Inputs:
            # 1D arrays, sorted, signed, -10^6 <= nums1[i], nums2[i] <= 10^6
            # 0 <= m <= 1000 -> What happens if both are zero?
            # Are the values unique??



        # Output:
            # median: float, signed, in theory -10^6 <= median <= 10^6
            # What happens on no return? 