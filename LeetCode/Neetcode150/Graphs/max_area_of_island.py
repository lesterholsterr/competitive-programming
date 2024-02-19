# Overall: This is good practice. BFS and DFS for graph questions seem pretty formulaic. 

import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        visited = set()

        # Initial Solution: Took a few tries but I remember the solution from Number of Islands
        def bfs(land):
            # We only call bfs on unvisited land tiles
            q = collections.deque()
            q.append(land)
            cur_island = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while q:
                x, y = q.popleft()
                if (x, y) not in visited:
                    cur_island += 1
                    visited.add((x, y))

                    for dx, dy in directions:
                        x1, y1 = x + dx, y + dy
                        if (0 <= x1 and x1 < len(grid[0]) and
                            0 <= y1 and y1 < len(grid) and
                            (x1, y1) not in visited and grid[y1][x1] == 1):
                            q.append((x1, y1))
                            
            return cur_island
        
        # Neetcode Solution: DFS probably makes more sense here seeing as the thing we are returning
        # has a nice recursive relation (1 + dfs(neighbours))
        def dfs(land):
            x, y = land
            if (0 > x or x == len(grid[0]) or
                0 > y or y == len(grid) or
                (x, y) in visited or grid[y][x] == 0):
                return 0
            visited.add((x, y))
            return 1 + dfs((x, y+1)) + dfs((x, y-1)) + dfs((x+1, y)) + dfs((x-1, y))
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (x, y) not in visited and grid[y][x] == 1:
                    max_island = max(max_island, bfs((x, y)))
        
        return max_island