# Easy greedy solution
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        maxfreq = 0
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
            maxfreq = max(maxfreq, freq[t])
        
        nummax = 0
        for x in freq.values():
            if x == maxfreq:
                nummax += 1

        return max((maxfreq-1)*(n+1) + nummax, len(tasks))
    
# Neetcode - heap
# Idea: processes are anonymous, we only care about frequencies
# Always run the process with the highest frequency whenever possible - so max heap data structure
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        q = deque()

        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        while heap or q:
            time += 1

            if not heap:
                time = q[0][1]				# not 100% sure how this is always guaranteed to work (what if there's >1 thing in the q?)
            else:
                c = 1 + heapq.heappop(heap) # we store them as negatives, so this is "decrementing"
                if c:					    # if c = 0, we have ran the process enough times
                    q.append([c, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
            
        return time