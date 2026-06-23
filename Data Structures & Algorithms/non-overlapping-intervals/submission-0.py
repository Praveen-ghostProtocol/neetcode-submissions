class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        removed = 0
        prevend = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prevend:
                removed += 1
            else:
                prevend = end
        
        return removed