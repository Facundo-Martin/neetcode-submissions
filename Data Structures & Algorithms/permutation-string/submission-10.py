class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        target_counts = [0] * 26
        window_counts = [0] * 26

        # Initialize counts for s1 and the first window of s2
        for i in range(m):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1

        # Calculate how many alphabet slots initially match perfectly
        matches = 0
        for i in range(26):
            if s1_counts[i] == window_counts[i]:
                matches += 1

        # Slide the window across s2
        for i in range(m, n):
            if matches == 26:
                return True
                
            # 1. Process character entering on the right
            r_idx = ord(s2[i]) - ord('a')
            window_counts[r_idx] += 1
            if window_counts[r_idx] == s1_counts[r_idx]:
                matches += 1
            elif window_counts[r_idx] == s1_counts[r_idx] + 1:
                matches -= 1
                
            # 2. Process character leaving on the left
            l_idx = ord(s2[i - m]) - ord('a')
            window_counts[l_idx] -= 1
            if window_counts[l_idx] == s1_counts[l_idx]:
                matches += 1
            elif window_counts[l_idx] == s1_counts[l_idx] - 1:
                matches -= 1

        return matches == 26
