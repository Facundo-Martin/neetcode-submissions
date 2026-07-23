class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        target_count = [0] * 26
        window_count = [0] * 26

        # Populate target frequencies
        for char in s1:
            target_count[ord(char) - ord('a')] += 1

        # Populate first window frequencies
        for i in range(m):
            window_count[ord(s2[i]) - ord('a')] += 1

        # Check if initial window matches
        if target_count == window_count:
            return True

        # Implement sliding window mechanism
        for i in range(n - m):
            # Drop the character at the left boundary
            window_counts[ord(s2[i - 1]) - ord('a')] -= 1
            
            # Add the new character entering m steps ahead
            window_counts[ord(s2[i + m]) - ord('a')] += 1

            if target_count == window_count:
                return True

        return False
