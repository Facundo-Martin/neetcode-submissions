class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        # Build frequency map for target (s)
        target_freq = {}
        for ch in t:
            target_freq[ch] = target_freq.get(ch, 0) + 1

        min_len = float('inf')
        result = ""
        n = len(s)

        # Create every possible substring combination using nested loop
        for i in range(n):
            for j in range(i + 1, n):
                substring = s[i: j + 1]

                # Build frequency map for substring
                window_freq = {}
                for ch in substring:
                    window_freq[ch] = window_freq.get(ch, 0) + 1

                # Check if window is valid. Update answer if needed.
                is_valid_window = True
                for char in target_freq:
                    if window_freq.get(char, 0) < target_freq[char]:
                        is_valid_window = False

                if is_valid_window:
                    if len(substring) < min_len:
                        min_len = len(substring)
                        result = substring 

        return result


