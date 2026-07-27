class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        
        # Count how many tasks have this exact maximum frequency
        max_count = sum(1 for v in counts.values() if v == max_freq)
        
        # Calculate the mathematical minimum (accounting for forced idles)
        time = (max_freq - 1) * (n + 1) + max_count
        
        # Return the larger of our formula or the total number of tasks
        return max(len(tasks), time)