class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []    # Collects all valid combination copies
        state = []      # Tracks the current combination being built

        def backtrack(start_index: int, current_sum: int):
            # Base Case: Valid combination found
            if current_sum == target:
                results.append(state.copy())
                return
            
            # Pruning: Short-circuit if sum exceeds target
            if current_sum > target:
                return

            # Recursively iterate over available choices
            for i in range(start_index, len(nums)):
                state.append(nums[i])                       # CHOOSE: Add current number
                backtrack(i, current_sum + nums[i])         # EXPLORE: Reuse 'i' for unlimited choices
                state.pop()                                 # UNCHOOSE: Backtrack for next loop
        
        # Start backtracking at index 0 with a starting sum of 0
        backtrack(0, 0)
        
        return results


        # =================================
        # ALGO DESIGN
        # =================================
        # Goal: Generate all unique combinations within the array (exhaustive search of state space)
        # Traversal strategy: Backtracking 
            # Time complexity: O(N^(T/M)) | N=len(nums), T=target, M=min(nums). Bound by max depth.
            # Space complexity: O(T/M) | Bound by max recursion call stack depth.
        # Failure mode: Empty paths or current sum exceeding target gracefully handled by pruning.
        # Edge cases:
            # Deduplication: Enforce forward-only traversal in get_available_choices to prevent permutations.
            # Infinite recursion: Prevented by positive integer constraints (sum strictly increases).
        # Short circuit (Pruning): Abandon branch immediately when state becomes invalid (sum > target).

        
        # =================================
        # PROBLEM SCOPING
        # =================================
        # Input:
            # nums: array, distinct integers, unsigned, non-sorted.
                # Bounds: 1 <= nums.length <= 20, 2 <= nums[i] <= 30.
            # target: unsigned integer.
                # Bounds: 2 <= target <= 30.
        # Constraints:
            # Generate valid combinations that sum to target.
            # Same candidate is reusable infinitely.
            # Frequency of elements defines uniqueness (order doesn't matter).
        # Output:
            # results: 2D array, unique valid combinations.