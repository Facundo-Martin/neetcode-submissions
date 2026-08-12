class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        # Mapping of phone digits to corresponding letters
        KEYPAD = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []
        state = []

        def backtrack(index: int):
            # Base case: completed a full string of length equal to input digits
            if len(state) == len(digits):
                res.append("".join(state))
                return

            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            possible_letters = KEYPAD[current_digit]

            for letter in possible_letters:
                state.append(letter)       # Make decision
                backtrack(index + 1)       # Move to the next digit
                state.pop()                # Undo decision (backtrack)

        backtrack(0)
        return res