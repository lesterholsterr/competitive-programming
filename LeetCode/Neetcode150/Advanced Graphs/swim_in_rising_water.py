# https://leetcode.com/problems/swim-in-rising-water/description/

# Initial - Nice!
# Only optimization is that there's no need to build an adjacency list from scratch
# Just check the 4 potential neighbours of the cell you are on
# That means you store the coordinates of the cell rather than its value though
from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        - find the path with the smallest max value -> seems familiar?
        - work backwards and greedily BFS?
        - DFS might be better, we need to keep track of visited cells
        - Actually... we can use Dijkstra and have the "weight" be the max value in the path!
        """
        n = len(grid)
        if n == 1:
            return grid[0][0]
        
        adj = defaultdict(list)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(n):
                for di, dj in directions:
                    i2, j2 = i+di, j+dj
                    if 0 <= i2 < n and 0 <= j2 < n:
                        adj[grid[i][j]].append(grid[i2][j2])
        
        # Dijkstra
        unvisited = set(adj.keys())
        paths = [(grid[0][0], grid[0][0])] # min heap -> (weight, cell)
        res = [float('inf')] * (n ** 2)

        while unvisited:
            while True:
                w, v = heappop(paths)
                if v in unvisited:
                    unvisited.remove(v)
                    break
            res[v] = min(res[v], w)
            for x in adj[v]:
                heappush(paths, (max(res[v], x), x))

        return res[grid[n-1][n-1]]
