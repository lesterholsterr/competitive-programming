# Initial - not much to say. i'm sure you can make it shorter.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        addedNew = False

        if not intervals:
            return [newInterval]

        for s, e in intervals:
            if e < newInterval[0]:
                ans.append([s, e])
            elif not addedNew:
                newInterval[0] = min(newInterval[0], s)
            else:
                ans.append([s, e])
            
            if newInterval[1] < s and not addedNew:
                ans.append(newInterval)
                ans.append([s, e])
                addedNew = True
            elif newInterval[1] <= e and not addedNew:
                ans.append([newInterval[0], e])
                addedNew = True
        
        if not addedNew:
            ans.append(newInterval)
        
        return ans
    
# Neetcode - outline the cases where newInterval DOESN'T overlap and everything else can go inside an else case. Smart.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(intervals)):
            a, b = newInterval
            if b < intervals[i][0]: # we've fully passed the new interval
                ans.append(newInterval)
                return ans + intervals[i:] # short circuit, so we can hard code an append at the end of the for loop
            elif a > intervals[i][1]: # still before the new interval
                ans.append(intervals[i])
            else: # "catch all" for when there is any overlap!
                newInterval[0] = min(a, intervals[i][0])
                newInterval[1] = max(b, intervals[i][1])
        
        ans.append(newInterval)
        return ans

# Revisited - this is probably most intuitive and readable solution
# There are 3 states - no overlap yet, overlap, overlap finished
# First while loop handles the "no overlap yet"
# Second while loop handles the "overlap"
# Third state is handled in the return statement
class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        return res + intervals[i:]