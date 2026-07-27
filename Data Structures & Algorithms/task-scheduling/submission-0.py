class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        
        # Python only has min-heaps, so we negate the frequencies
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()  # Store pairs: [remaining_frequency, available_time]
        
        while maxHeap or q:
            time += 1
            
            if maxHeap:
                # Pop the most frequent available task
                # Add 1 because it's negative (e.g., -3 + 1 = -2)
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    # It still has runs left, park it in the queue
                    q.append([cnt, time + n])
            
            # If the queue has a task whose cooldown is over, put it back in the heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time