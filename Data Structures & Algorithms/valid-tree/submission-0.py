class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        q = deque([0])
        visited.add(0)

        while q:
            node = q.popleft()

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return len(visited) == n

        