class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1] # Note that right side is non-inclusive when using : method
            i, j, k = L, 0, 0   

            # Implement conquer strategy
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else: 
                    arr[i] = right[k]
                    k += 1
                i += 1

            # Add remaining left half values to array (if needed)
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            # Add remaining right half values to array (if needed)
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1
            

        def mergeSort(arr, l, r):
            # Base case
            if l == r:
                return

            m = (l + r) // 2
            mergeSort(arr, l, m) # Left half of the array
            mergeSort(arr, m + 1, r) # Right half of the array

            merge(arr, l, m, r)
            return arr
        
        # Initial call with entire array
        return mergeSort(nums, 0, len(nums) - 1) 