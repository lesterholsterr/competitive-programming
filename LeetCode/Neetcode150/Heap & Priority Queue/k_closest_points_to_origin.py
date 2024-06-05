# no comment, could have used heapify but I think there is no functional difference
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            heapq.heappush(distances, (p[0]**2 + p[1]**2, p))

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(distances)[1])
        return ans
