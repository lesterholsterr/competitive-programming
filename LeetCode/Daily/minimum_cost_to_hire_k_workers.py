# Initial: Doesn't work. Sometimes it's better to hire workers with worse "value" just because their
# quality is lower (they can still be nominally cheaper despite being paid at a higher rate)
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        value = {}  # value (float) -> indices (List[int])
        heap = []  # stores values (float)
        for i in range(len(quality)):
            v = round(wage[i] / quality[i], 6)
            if v in value:
                value[v].append(i)
            else:
                value[v] = [i]
            heappush(heap, v)
        print(value)
        hiring = []  # indices of the workers we are hiring
        v = 0
        while len(hiring) != k:
            v = heappop(heap)
            workers = value[v]
            while workers and len(hiring) != k:
                hiring.append(workers.pop())

        cost = 0
        for i in hiring:
            cost += quality[i] * v
        return cost

# Actual
# Premise: We should hire many, but not all, of the most 'value' workers. Start with that, and see if any higher rate workers can replace the highest rate worker currently being hired.
# Credit: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/?envType=daily-question&envId=2024-05-11
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        value = sorted([(w / q, q) for w, q in zip(wage, quality)])
        max_heap = []
        total_quality = 0
        max_value = 0.0

        for i in range(k):
            max_value = max(max_value, value[i][0])
            total_quality += value[i][1]
            heapq.heappush(max_heap, -value[i][1])
        
        res = max_value * total_quality

        for i in range(k, len(quality)):
            max_value = max(max_value, value[i][0])
            total_quality += value[i][1] + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -value[i][1])
            res = min(res, max_value * total_quality)
        
        return res