# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# Mistakes
# - Tried to save the wrong thing in the dp matrix
# - Used a visited set for 'backtracking' - useless beacuse paths are strictly increasing
#   - ^It's DFS not backtracking!
# Intuition: Pretty clear 2D-DP. Bottom-up solution is not intuitive but it actually involves sorting, so this is good enough.

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(x, y):
            if dp[x][y] != -1:
                return dp[x][y]
            max_path = 1
            for dx, dy in directions:
                if (0 <= x+dx < m and 0 <= y+dy < n and matrix[x+dx][y+dy] > matrix[x][y]):
                    max_path = max(1 + dfs(x+dx, y+dy), max_path)
            dp[x][y] = max_path
            return max_path
        
        max_path = 0
        for i in range(m):
            for j in range(n):
                max_path = max(dfs(i, j), max_path)
        return max_path