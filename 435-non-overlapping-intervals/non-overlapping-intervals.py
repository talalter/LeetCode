class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda x: x[1])
        current_start = intervals[0][0]
        current_end = intervals[0][1]
        for start, end in intervals[1:]:
            if current_end > start:
                res += 1
            else:
                current_end = end
        return res 

