# Overall: Split the problem into 2 parts - label the squares that can flow to the pacific
# and label the squares for atlantic. Answer is the overlap.
# These subproblems are easily solved with conventional DFS.

# Attempt 1 - idk what i'm doing
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited, pacific, atlantic = set(), set(), set()  # [int, int]
        ans = []

        def isPacific(cords):
            r, c = cords
            return r == 0 or c == 0

        def isAtlantic(cords):
            r, c = cords
            return r == len(heights) or c == len(heights[0])

        def search(cords):
            flowPacific, flowAtlantic = isPacific(cords), isAtlantic(cords)
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visited.add(cords)
            r, c = cords

            for dr, dc in directions:
                r1, c1 = r + dr, c + dc
                cords1 = [r1, c1]

                if (r1 >= 0 and r1 < len(heights) and
                    c1 >= 0 and c1 < len(heights[0]) and
                    heights[r][c] >= heights[r1][c1] and
                        cords1 not in visited):
                    search(cords1)
                    if cords1 in pacific:
                        pacific.add(cords)
                        flowPacific = True
                    if cords1 in atlantic:
                        atlantic.add(cords)
                        flowAtlantic = True

            if flowPacific and flowAtlantic:
                ans.append(cords)

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                cords = [r, c]
                if cords not in visited:
                    search(cords)

        return ans

# Attempt 2 - still dk what's going on


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()  # [int, int]
        ans = []

        def searchPacific(cords):
            directions = [[1, 0], [0, 1]]
            q = collections.deque(cords)

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    r1, c1 = r + dr, c + dc
                    cords1 = [r1, c1]

                    if (r1 >= 0 and r1 < len(heights) and
                        c1 >= 0 and c1 < len(heights[0]) and
                            heights[r][c] <= heights[r1][c1]):
                        pacific.add(cords1)
                        q.append(cords1)

        def searchAtlantic(cords):
            directions = [[-1, 0], [0, -1]]
            q = collections.deque(cords)

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    r1, c1 = r + dr, c + dc
                    cords1 = [r1, c1]

                    if (r1 >= 0 and r1 < len(heights) and
                        c1 >= 0 and c1 < len(heights[0]) and
                            heights[r][c] <= heights[r1][c1]):
                        atlantic.add(cords1)
                        q.append(cords1)

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                cords = [r, c]
                if cords in pacific and cords in atlantic:
                    ans.append(cords)

        return ans

# Neetcode Solution


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()  # (int, int)
        ans = []

        def dfs(r, c, visited, h):
            if (r in range(ROWS) and
                c in range(COLS) and
                (r, c) not in visited and
                    heights[r][c] >= h):
                visited.add((r, c))
                dfs(r+1, c, visited, heights[r][c])
                dfs(r-1, c, visited, heights[r][c])
                dfs(r, c+1, visited, heights[r][c])
                dfs(r, c-1, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans
