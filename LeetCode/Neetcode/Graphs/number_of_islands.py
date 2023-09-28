# Neetcode Solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = []
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands


# My Solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if (grid[r][c] == "1" and
                        (r, c) not in visited):
                    islands += 1
                    visited.add((r, c))
                    q = deque([(r, c)])
                    while q:
                        r0, c0 = q.popleft()
                        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                        for r1, c1 in directions:
                            r2, c2 = r0 + r1, c0 + c1
                            if r2 < row and r2 >= 0 and c2 < col and c2 >= 0 and grid[r2][c2] == "1" and (r2, c2) not in visited:
                                q.append((r2, c2))
                                visited.add((r2, c2))

        return islands
