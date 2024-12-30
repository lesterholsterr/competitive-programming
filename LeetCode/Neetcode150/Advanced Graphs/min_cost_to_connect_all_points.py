# https://leetcode.com/problems/min-cost-to-connect-all-points/

# New type of problem: Minimum Spanning Tree
# Requires: Adjacency list of edges + their weights
# - In this case we have to build this list ourselves
# Algorithm: Prim's (although I think there is something else called Kruskal's? Worth revisiting.)

from heapq import heappush, heappop

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = { i : [] for i in range(n) }
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                md = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((md, j))
                adj[j].append((md, i))
        
        min_cost = 0
        visited = set()
        frontier = [[0, 0]]
        while len(visited) < n:
            cost, node = heappop(frontier)
            if node in visited:
                continue
            visited.add(node)
            min_cost += cost
            for nei_cost, nei_node in adj[node]:
                heappush(frontier, (nei_cost, nei_node))
        return min_cost
