# Reverse the question. Instead of how far each land is from treasure, how far is treasure from each land?
# Leads to a BFS solution where the queue is initialized with all the treasures, and we "fan out" from there
import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        def addCell(x, y):
            if (
                0 <= x and x < len(grid) and
                0 <= y and y < len(grid[0]) and
                (x, y) not in visited and
                grid[x][y] != -1
            ):
                q.append((x, y))
                visited.add((x, y))
        
        d = 0
        while q:
            l = len(q)
            for i in range(l):
                x, y = q.popleft()
                grid[x][y] = d
                addCell(x+1, y)
                addCell(x-1, y)
                addCell(x, y+1)
                addCell(x, y-1)
            d += 1