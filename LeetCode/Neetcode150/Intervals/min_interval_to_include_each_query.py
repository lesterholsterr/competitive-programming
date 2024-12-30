# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/
# Too lazy to implement brute force. Couldn't find the min heap solution myself, even with hints
# Intuition
# - consider both the intervals and queries in ascending order (theme for interval questions - do this and iterate "monotonically")
# - for a given q, we can ignore all intervals that start after q
# - for the intervals we do consider, we want to choose the one with the smallest size -> now min heap is obvious
# - implementation is fairly straightforward. one nuance is that weneed to add new intervals before removing old
#   - interesting edge case where an irrelevant intermediate interval may be added. must be discarded before we process the query.

from heapq import heappush, heappop

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = []
        res = {}
        i = 0
        for q in sorted(queries):
            # add intervals that are in range
            while i < len(intervals) and q >= intervals[i][0]:
                size = intervals[i][1] - intervals[i][0] + 1
                heappush(heap, (size, intervals[i][1]))
                i += 1
            # remove intervals that are no longer in range
            while heap and q > heap[0][1]:
                heappop(heap)
            
            if q in res:
                continue
            res[q] = heap[0][0] if heap else -1
        
        return [res[q] for q in queries]