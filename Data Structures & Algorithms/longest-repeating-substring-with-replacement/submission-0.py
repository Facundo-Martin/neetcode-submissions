class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = {}

            for j in range(i, n):
                # Update frequency counter
                freq[s[j]] = freq.get(s[j], 0) + 1

                # Grab window size and max_freq character
                max_freq = max(freq.values())
                window_size = j - i + 1


                # Check for valid window with only 1 character
                if window_size - max_freq <= k:
                    ans = max(ans, window_size)

        return ans