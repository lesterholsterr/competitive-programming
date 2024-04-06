# thoughts - all these graph problems feel the same once you identify whether bfs or dfs is needed,
#            which usually seems pretty obvious (or both would work)

# initial - took 2 tries, missed some edge cases
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def solved() -> bool:
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 1:
                        return False
            return True

        q = collections.deque()
        visited = set()
        minutes = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # <-- need include this check otherwise something like [[0]] would return -1
        if solved():
            return minutes

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))

        while q:
            if solved():
                return minutes
            minutes += 1
            n = len(q)
            for i in range(n):
                r, c = q.popleft()
                for dr, dc in directions:
                    r1, c1 = r + dr, c + dc
                    if (r1 >= 0 and r1 < ROWS and c1 >= 0 and c1 < COLS and
                            (r1, c1) not in visited and grid[r1][c1] == 1):
                        grid[r1][c1] = 2
                        q.append((r1, c1))
                        visited.add((r1, c1))
        return -1

# neetcode
# - using a variable to count # of oranges is a lot smarter than doing a scan every iteration
# - also, there's no need for a visited set since we're essentially "marking" oranges by
#   making them rotten when we visit them
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        minutes = 0
        fresh = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        while fresh > 0 and q: # <-- note the compound condition for the while loop
            minutes += 1
            n = len(q)
            for i in range(n):
                r, c = q.popleft()
                for dr, dc in directions:
                    r1, c1 = r + dr, c + dc
                    if (
                        r1 in range(ROWS) and  # <-- syntactic sugar
                        c1 in range(COLS) and
                        grid[r1][c1] == 1
                    ):
                        fresh -= 1
                        grid[r1][c1] = 2
                        q.append((r1, c1))
        return minutes if fresh == 0 else -1