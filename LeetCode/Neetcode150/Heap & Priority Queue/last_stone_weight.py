# thoughts
# not much learned here, easy level question after all

# initial
# i only know how to do minheap so just made everything negative to make a max heap...
# Update: That is actually how you do max heap in Python lol
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, -abs(a-b))
        return -stones[0] if stones else 0