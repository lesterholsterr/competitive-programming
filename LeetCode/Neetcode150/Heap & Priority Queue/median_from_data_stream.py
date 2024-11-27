# https://leetcode.com/problems/find-median-from-data-stream/
# Getting better with handling edge cases. Talking out loud helps somewhat?
import heapq

class MedianFinder:

    def __init__(self):
        self.lo = [] # max heap
        self.hi = [] # min heap
        self.lo_size = 0
        self.hi_size = 0

    def addNum(self, num: int) -> None:
        # if both are empty, insert into lo (arbitrary)
        # if hi is empty and num > lo[0], insert into hi
        # if hi is empty and num < lo[0], move lo[0] to hi, then insert into lo
        # otherwise, neither is empty
        # - if num < lo[0] or num > hi[0], insert into that one
        # - BUT it after inserting, lo_size and hi_size would differ by >1
        #   move one from the bigger to the smaller heap
        #   then insert your num where it belongs
        # - if it's between those values, insert into the smaller one. if equal size, then lo (arbitrary).
        
        # Both empty
        if not self.lo:
            heapq.heappush(self.lo, -num)
            self.lo_size += 1
        # hi empty
        elif not self.hi and num >= -self.lo[0]:
            heapq.heappush(self.hi, num)
            self.hi_size += 1
        elif not self.hi: # Implied num < self.lo[0]
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
            heapq.heappush(self.lo, -num)
            self.hi_size += 1
        # neither empty
        elif num > self.hi[0]:
            heapq.heappush(self.hi, num)
            self.hi_size += 1
        else: # Implied num < self.hi[0]
            heapq.heappush(self.lo, -num)
            self.lo_size += 1
        
        if self.lo_size - self.hi_size > 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
            self.lo_size -= 1
            self.hi_size += 1
        elif self.hi_size - self.lo_size > 1:
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
            self.lo_size += 1
            self.hi_size -= 1

    def findMedian(self) -> float:
        if (self.lo_size + self.hi_size) % 2 == 0:
            return (-self.lo[0] + self.hi[0]) / 2
        elif self.lo_size > self.hi_size:
            return -self.lo[0]
        return self.hi[0]