class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [0] * n

        def dfs(node):
            visited[node] = 1

            for nei in graph[node]:
                if visited[nei] == 0:
                    dfs(nei)

        components = 0

        for node in range(n):
            if visited[node] == 0:
                components += 1
                dfs(node)
        
        return components

        