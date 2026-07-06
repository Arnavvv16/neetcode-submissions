"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n == 0 :
            return True
        intervals.sort(key = lambda x: x.end)

        lastend = intervals[0].end
        cnt = 1

        for i in range(1,n):
            if intervals[i].start >= lastend :
                cnt +=1
                lastend = intervals[i].end
        if cnt == n :
            return True
        return False