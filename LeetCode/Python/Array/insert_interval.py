class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        l = len(intervals)
        if l == 0:
            return [newInterval]

        result = []
        for interval in intervals:
            if newInterval[0] > interval[1]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        result.append(newInterval)
        return result