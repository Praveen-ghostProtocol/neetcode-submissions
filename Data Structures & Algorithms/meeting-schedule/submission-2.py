"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        prevstart = intervals[0].start
        prevend = intervals[0].end
        print(prevstart)
        print(prevend)
        for interval in intervals[1:]:
            if interval.start < prevend:
                return False
            prevstart = interval.start
            prevend = interval.end
        return True
