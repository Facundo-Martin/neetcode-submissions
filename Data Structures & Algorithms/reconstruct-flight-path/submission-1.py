import collections

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # 1. Build the graph
        graph = collections.defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
            
        # 2. Sort the destinations in reverse lexical order
        # Reverse sorting allows us to O(1) pop the smallest element from the end
        for src in graph:
            graph[src].sort(reverse=True)
            
        itinerary = []
        
        def dfs(airport):
            # While there are available flights, recursively visit the smallest one
            while graph[airport]:
                next_dest = graph[airport].pop()
                dfs(next_dest)
            
            # 3. We hit a dead end. Append to itinerary.
            itinerary.append(airport)
            
        dfs("JFK")
        
        # 4. Reverse the post-order traversal to get the actual path
        return itinerary[::-1]
