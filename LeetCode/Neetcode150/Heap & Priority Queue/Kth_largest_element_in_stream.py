# Overall: In hindsight I see how the heap data structure is useful. Min heap lets us repeatedly insert
# elements and remove the smallest element in log time (as opposed to linear for lists)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)  # O(logn)

        while len(self.minHeap) > k:  # Worst case runs n times
            heapq.heappop(self.minHeap)  # O(logn)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
