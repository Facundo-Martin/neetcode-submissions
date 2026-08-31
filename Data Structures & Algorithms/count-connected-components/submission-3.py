class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node: int) -> None:
            for nei in graph[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                dfs(nei)

        count = 0
        for node in range(n):
            # Skip already visited nodes
            if node in visited:
                continue

            visited.add(node)
            dfs(node)
            count += 1

        return count

