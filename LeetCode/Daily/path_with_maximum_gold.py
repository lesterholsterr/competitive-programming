# challenge here is how to keep an updated list of "visited" squares
# backtracking idea - update grid in place, make recursive calls, then undo the change in grid

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if (i < 0 or i >= m or
                j < 0 or j >= n or
                grid[i][j] == 0):
                return 0
            
            curgold = grid[i][j]
            grid[i][j] = 0 # <-- !!!
            maxgold = max(dfs(i+1, j),
                          dfs(i-1, j),
                          dfs(i, j+1),
                          dfs(i, j-1))
            grid[i][j] = curgold # <-- !!!
            return curgold + maxgold
        
        maxgold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    maxgold = max(dfs(i, j), maxgold)
        return maxgold