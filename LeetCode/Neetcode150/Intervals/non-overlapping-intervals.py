# https://leetcode.com/problems/non-overlapping-intervals/description/

# Initial: Greedy is correct, but was looking at the wrong metric
# How long technically doesn't matter. What matters is when it ends. 
# Easy to think of edge cases where comparing interval length breaks down
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy: it's always better to remove the larger of 2 overlapping intervals
        # but if multiple overlapping intervals, how do you know when you've seen the largest?
        # [1, 5], [2, 3], [2, 10], [4, 5]
        intervals.sort()
        removed = 0
        remaining = []
        for interval in intervals:
            if not remaining:
                remaining.append(interval)
                continue
            
            if remaining[-1][1] <= interval[0]:
                remaining.append(interval)
                continue
            
            removed_this = False
            while remaining and remaining[-1][1] > interval[0]:
                if remaining[-1][1] - remaining[-1][0] <= interval[1] - interval[0]:
                    removed += 1
                    removed_this = True
                    break
                else:
                    remaining.pop()
                    removed += 1
            if not removed_this:
                remaining.append(interval)
        return removed

# Works, but slow and O(n) memory
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removed = 0
        remaining = []

        for interval in intervals:
            if not remaining:
                remaining.append(interval)
                continue
            
            if remaining[-1][1] <= interval[0]:
                remaining.append(interval)
                continue
            
            removed_this = False
            while remaining and remaining[-1][1] > interval[0]:
                if remaining[-1][1] < interval[1]:
                    removed += 1
                    removed_this = True
                    break
                else:
                    remaining.pop()
                    removed += 1
            if not removed_this:
                remaining.append(interval)
        return removed
    
# Optimized. You don't need a stack of intervals if the end variable is always minimal (thanks to greedy)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removed = 0
        end = intervals[0][1]

        for interval in intervals[1:]:
            if end <= interval[0]:
                end = interval[1]
            else:
                removed += 1
                end = min(end, interval[1])
        
        return removed