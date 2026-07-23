class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Defensive programming (edge cases)
        # 2. Create pointer or for loop
        # 3. Traverse structures
        # 4. Implement checking logic for characters
        # 5. Return condition

        if len(s) != len(t):
            return False
        
        if len(s) == 0 or len(t) == 0:
            return False 

        for idx, x in enumerate(s):
            if x != t[len(s) - 1 -i]:
                return False

        return True
        