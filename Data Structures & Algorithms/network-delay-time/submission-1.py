class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((v,t))

        dist = [float('inf')] * (n+1)
        dist[k] = 0

        heap = [(0,k)]
        
        while heap:
            curr,node = heapq.heappop(heap)

            if curr > dist[node]:
                continue
            for nei, time in graph[node]:
                newtime = curr + time

                if newtime < dist[nei]:
                    dist[nei] = newtime
                    heapq.heappush(heap, (newtime, nei))
        
        max_time = max(dist[1:])
        return max_time if max_time != float('inf') else -1
        