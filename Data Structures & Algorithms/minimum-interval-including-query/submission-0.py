class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sortedqueries = sorted((q,i) for i,q in enumerate(queries))

        ans = [-1] * len(queries)
        heap = []

        i = 0
        n = len(intervals)

        for q,orig in sortedqueries:
            while i < n and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                i += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            if heap:
                ans[orig] = heap[0][0]
        return ans
