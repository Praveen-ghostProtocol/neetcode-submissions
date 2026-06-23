class Solution:
    def numIslands(self, graph: List[List[str]]) -> int:
        rows, cols = len(graph), len(graph[0])
        visited = set()
        count = 0

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>= cols or (r,c) in visited or graph[r][c] == '0':
                return
            visited.add((r,c))

            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for dr, dc in directions:
                nr,nc = r+dr, c+dc
                dfs(nr,nc)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and graph[r][c] == '1':
                    count += 1
                    dfs(r,c)
        return count