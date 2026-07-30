class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Lexically scoped variables (closures)
        results = []
        state = []
        current_sum = 0
        
        # start_index is passed as it strictly defines the branch constraint for the current frame
        def backtrack(start_index):
            nonlocal current_sum
            
            # Base Case 1: Complete and valid solution
            if current_sum == target:
                results.append(state.copy())
                return
            
            # Base Case 2: Pruning (Short-circuit invalid paths)
            if current_sum > target:
                return

            # Recursive case: Try available choices (forward-only to dedupe)
            for i in range(start_index, len(nums)):
                choice = nums[i]
                
                # 1. CHOOSE
                state.append(choice)
                current_sum += choice
                
                # 2. EXPLORE (Pass 'i' to allow unbounded reuse)
                backtrack(i)
                
                # 3. UNCHOOSE (Backtrack the state AND the sum)
                state.pop()
                current_sum -= choice

        # Init DFS traversal
        backtrack(start_index=0)
        
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