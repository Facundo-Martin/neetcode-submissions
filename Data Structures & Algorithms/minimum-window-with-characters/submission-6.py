class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        # Build frequency map for target (s)
        target_freq = {}
        for ch in t:
            target_freq[ch] = target_freq.get(ch, 0) + 1


        window_freq = {}
        required, formed = len(target_freq), 0
        res, resLen = [-1, -1], float("inf")
        n = len(s)
        l = 0

        # Traverse string with right pointer until we find a valid window
        for r in range(n):
            # Update window frequency
            ch = s[r]
            window_freq[ch] = window_freq.get(ch, 0) + 1
            
            # Mark character as satisfied if its frequency matches the target
            if ch in target_freq and target_freq[ch] == window_freq.get(ch, 0):
                formed += 1

            # Contract the window from the left once it is fully valid
            while required == formed:
                # Update minimum window if current is smaller
                window_size = r - l + 1
                if window_size < resLen:
                    resLen = window_size
                    res = [l, r]
                
                # Remove character from left of window (we know for sure it was in our window_freq)
                char = s[l]
                window_freq[char] -= 1

                # If removing this character breaks the target condition, decrement 'formed'
                if char in target_freq and window_freq.get(char) < target_freq.get(char):
                    formed -= 1

                l += 1





        return "" if min_len == float('inf') else s[min_left:min_right + 1]


