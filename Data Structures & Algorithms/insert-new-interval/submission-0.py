class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        n = len(intervals)

        newstart, newend = newInterval
        while i<n and intervals[i][1] < newstart:
            ans.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newend:
            newstart = min(newstart, intervals[i][0])
            newend = max(newend, intervals[i][1])
            i+=1
        
        ans.append([newstart,newend])

        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans