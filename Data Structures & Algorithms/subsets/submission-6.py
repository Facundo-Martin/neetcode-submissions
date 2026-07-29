class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []  # Collects all valid subset copies
        state = []    # Tracks the current state being built

        def backtrack(start_index: int):
            results.append(state.copy())    # Base case: Every state is a valid subset

            # Recursively iterate over valid options
            for i in range(start_index, len(nums)):
                state.append(nums[i])       # CHOOSE: Add current number
                backtrack(i + 1)            # EXPLORE: Move to next index
                state.pop()                 # UNCHOOSE: Backtrack for next loop
        
        # Start backtracking at index 0
        backtrack(0)
        
        return results

        # ==================================================
        # DRY RUN: nums = [1, 2]
        # ==================================================
        # Initialize: results = [], state = []

        # Call: backtrack(0)
        # results.append(state.copy()) -> results = [[]]

        # Loop i = 0 (nums[0] = 1):
        #     CHOOSE: state.append(1)    -> state = [1]
        #     EXPLORE: backtrack(1)
            
        #     Inside backtrack(1):
        #     results.append(state.copy()) -> results = [[], [1]]
            
        #     Loop i = 1 (nums[1] = 2):
        #         CHOOSE: state.append(2)    -> state = [1, 2]
        #         EXPLORE: backtrack(2)
                
        #         Inside backtrack(2):
        #         results.append(state.copy()) -> results = [[], [1], [1, 2]]
        #         Loop range(2, 2) is empty. Return.
                
        #         UNCHOOSE: state.pop()      -> state = [1]
            
        #     UNCHOOSE: state.pop()      -> state = []

        # Loop i = 1 (nums[1] = 2):
        #     CHOOSE: state.append(2)    -> state = [2]
        #     EXPLORE: backtrack(2)
            
        #     Inside backtrack(2):
        #     results.append(state.copy()) -> results = [[], [1], [1, 2], [2]]
        #     Loop range(2, 2) is empty. Return.
            
        #     UNCHOOSE: state.pop()      -> state = []

        # END
        # Final Output: [[], [1], [1, 2], [2]]

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
        