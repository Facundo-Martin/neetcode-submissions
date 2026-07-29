class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Collects all valid subsets
        results = []

        # Backtracking function to build subsets recursively
        def backtrack(state: List[int], start_index: int):
            # Base case: Every state is a valid subset, so store a copy
            results.append(list(state))

            # Recursive case: Try each available choice moving forward
            for i in range(start_index, len(nums)):
                # 1. CHOOSE: Add the current number to the state
                state.append(nums[i])

                # 2. EXPLORE: Recursively build the next level of the subset
                backtrack(state, i + 1)

                # 3. UNCHOOSE: Backtrack by popping the last element to try the next loop iteration
                state.pop()
        
            
        # Start backtracking with an empty state at index 0
        backtrack([], 0)
        
        return results

    # Algorithm Design
        # Identity: Generate all combinations (Power Set).
        # Traversal method: Backtracking (DFS) with a moving index.
        # Complexity:
            # Time: O(N * 2^N). There are 2^N subsets, and copying each to 'results' takes up to O(N).
            # Space: O(N). The max depth of the recursion tree (call stack) is N. (Excludes output array).
        # Edge cases & Handling:
            # [3,2,1] == [1,2,3]: [Redundant] Because our DFS loop strictly uses 'i + 1', we only 
            #   ever move rightward through the array. We will physically never generate [3,2,1]. 
            # len(nums) == 1: Handled automatically. The loop runs once, adds the item, 
            #   recurses out of bounds (which terminates), and pops. Result: [[], [nums[0]]].
            # Empty subset []: Handled automatically by our base case logic appending the 
            #   initial empty 'current_path' before the loop even starts.
        # Short circuit: None, need to create all subsets. Stops at i == len(nums)
        # State: res (output array), index (integer), current_path (list array).
    
    # ==========================================
    # PROBLEM SCOPING
    # ==========================================

    # Constraints & Invariants
        # "return all possible subsets" -> Generate the Power Set -> Leaning backtracking algo
        # No duplicate subsets allowed in the final output.

    # Inputs
        # nums: arr, signed int, unique ints, -10 <= nums[i] <= 1, 1 <= nums.length <= 10
        # Def programming: If len(nums) == 0, then the options are [[],[nums[i]]]
        # Edge case: An empty array is ALWAYS a valid subset
        # No need to check for duplicate nums


    # Outputs
        # res: arr of arr, all possible subsets of nums, no duplicate sets
            # Def programming: Sort then check for equality! 
            # [3,2,1] is equal to [1,2,3] for this problem
        