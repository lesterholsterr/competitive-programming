# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

# Initial - Read first hint on Neetcode, but otherwise independent solution!
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijkjstra red herring. Use k iterations of BFS.
        adj = defaultdict(list)
        for f, t, p in flights:
            adj[f].append((t, p))
        
        q = deque()
        q.append((src, 0))
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            l = len(q)
            for _ in range(l):
                n, c = q.popleft()
                for nei_n, nei_c in adj[n]:
                    cur_c = prices[nei_n]
                    if c + nei_c < cur_c:
                        prices[nei_n] = c + nei_c
                        q.append((nei_n, c + nei_c))

        return prices[dst] if prices[dst] != float('inf') else -1

# Neetcode - Bellman-Ford algorithm
# Slightly slower, but more readable BFS (basically instead of a queue, consider all edges each time)
# Also you don't need to build the adjacency list, so it's O(n) memory rather than O(n^2)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            prices_copy = prices.copy()
            for f, t, p in flights:
                if prices[f] == float('inf'):
                    continue
                elif prices[f] + p < prices_copy[t]:
                    prices_copy[t] = prices[f] + p
            prices = prices_copy

        return prices[dst] if prices[dst] != float('inf') else -1
