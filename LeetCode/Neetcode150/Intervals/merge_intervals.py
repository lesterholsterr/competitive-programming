# https://leetcode.com/problems/merge-intervals/

# Not bad. 1 mistake (see below)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [[1,3],[2,6],[8,10],[15,18]]
        cur [8, 10]
        res [[1, 6], [8, 10]]

        cur[0] = intervals[i][0]
        cur[1] = max(intervals[i][1], intervals[i+1][1]) if intervals[i][1] >= intervals[i+1][0] (overlap)
        append cur, new cur[0] = intervals[i][0] and repeat
        """
        intervals.sort()
        i = 0
        res = []
        cur = [-1, -1]
        while i < len(intervals):
            if cur[0] == -1:
                cur[0] = intervals[i][0]
                cur[1] = intervals[i][1]
            
            if i < len(intervals) - 1 and cur[1] >= intervals[i+1][0]: # <-- 1 mistake - used intervals[i][1] instead of cur[1]
                cur[1] = max(cur[1], intervals[i+1][1])
            else:
                res.append(cur)
                cur = [-1, -1]
            
            i += 1
        
        return res
    
# Same idea but cleaner
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        cur = intervals[0]
        for interval in intervals[1:]:
            if cur[1] >= interval[0]:
                cur[1] = max(cur[1], interval[1])
            else:
                res.append(cur)
                cur = interval
        res.append(cur)
        return res