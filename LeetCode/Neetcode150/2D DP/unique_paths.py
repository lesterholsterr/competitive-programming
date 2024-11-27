# Pretty clear bottom-up solution, not much to say
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1]*n for _ in range(m)]
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                paths[i][j] = paths[i+1][j] + paths[i][j+1]
        
        return paths[0][0]