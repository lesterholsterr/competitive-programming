# https://leetcode.com/problems/network-delay-time/

# Initial - clear Dijkstra application
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(1, n+1)}
        for u, v, w in times:
            adj[u].append((v, w))
        
        time = [float('inf')] * (n+1)
        time[0] = 0
        time[k] = 0
        unvisited = set(list(range(1, n+1)))
        cur_node = k
        cur_time = time[cur_node]

        while unvisited:
            unvisited.remove(cur_node)
            for v, w in adj[cur_node]:
                time[v] = min(time[v], cur_time + w)

            min_time = float('inf')
            min_node = 0
            for node in unvisited:
                if time[node] <= min_time:
                    min_time = time[node]
                    min_node = node
            
            cur_node = min_node
            cur_time = min_time
        
        return max(time) if max(time) != float('inf') else -1

# Better, using heap (although Leetcode says this is slower?)
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        heap = [(0, k)]
        unvisited = set(list(range(1, n+1)))
        max_time = 0

        while heap:
            t, n = heappop(heap)
            if n in unvisited:
                unvisited.remove(n)
                max_time = max(max_time, t)
                for v, w in adj[n]:
                    heappush(heap, (t + w, v))
        
        return max_time if not unvisited else -1