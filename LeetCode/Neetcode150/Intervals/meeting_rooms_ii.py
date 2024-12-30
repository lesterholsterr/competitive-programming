# https://leetcode.com/problems/meeting-rooms-ii/description/
# Came very close but tunnel visioned on the data structure
# Intuition for heap: Given the start time of the next meeting, we need to
# know which of the currently occupied meeting rooms will end *first* and at what time.

# Initial - doesn't pass all cases...
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # min rooms = max overlap at any point
        # stack to track overlapping meetings
        # sort and linear scan like meeting rooms 1
        intervals.sort()
        stack = []
        rooms = 0

        for interval in intervals:
            while stack and stack[-1][1] <= interval[0]:
                stack.pop()
            stack.append(interval)
            rooms = max(rooms, len(stack))

        return rooms

# Solution
# Wrong data structure! Needed a heap. That's all.
from heapq import heappop, heappush

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        rooms = 0

        for interval in intervals:
            while heap and heap[0] <= interval[0]:
                heappop(heap)
            heappush(heap, interval[1])
            rooms = max(rooms, len(heap))

        return rooms