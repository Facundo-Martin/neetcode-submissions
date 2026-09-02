from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
            
        for src in graph:
            graph[src].sort(reverse=True)
            
        stack = ["JFK"]
        itinerary = []
        
        while stack:
            # Look at the current airport at the top of the stack
            curr = stack[-1]
            
            # If there are flights left from this airport, go to the next one
            if graph[curr]:
                stack.append(graph[curr].pop())
            # If no flights are left, this is a dead end. Pop it to the result.
            else:
                itinerary.append(stack.pop())
                
        return itinerary[::-1]