class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u,v,price in flights:
            graph[u].append((v,price))
        
        q = deque([(0,src,0)])
        dist = [float('inf')] * n
        dist[src] = 0

        while q:
            stops, node, cost = q.popleft()

            if stops > k:
                continue
            
            for nei,price in graph[node]:
                newcost = cost + price
                if newcost < dist[nei]:
                    dist[nei] = newcost
                    q.append((stops+1, nei, newcost))
        
        return -1 if dist[dst] == float('inf') else dist[dst]