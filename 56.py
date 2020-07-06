class Solution:
    def merge(self, intervals: [list]) -> [list]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        res = []
        part = []
        part.append(intervals[0][0])
        part.append(intervals[0][1])
        for i in intervals[1:]:
            if i[0] <= part[1]:
                part[1] = i[1] if i[1] > part[1] else part[1]
            else:
                res.append(part)
                part = i
        res.append(part)
        return res
