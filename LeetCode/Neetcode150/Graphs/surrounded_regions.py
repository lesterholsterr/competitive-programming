# thoughts
# - Concept: Reverse thinking. There are always 2 ways of specifying what you want.
#   1. "Only A"
#   2. "Everything except (NOT A)"
# - Turn "I only want to flip surrounding regions" into "I want to flip every region except
#   the non-surrounded (i.e. border) regions"
# - Now all you have to do is mark the border regions and blindly mark everything else as an 'X'

# Initial: Memory exceeded? Never had that problem before 🤔
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def bfs(coords):
            isEdge = False
            visited.add(coords)
            flip = [coords]
            q = collections.deque()
            q.append(coords)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                r, c = q.popleft()
                if r == 0 or r == ROWS-1 or c == 0 or c == COLS-1:
                    isEdge = True
                for dr, dc in directions:
                    r1, c1 = r + dr, c + dc
                    if (r1 >= 0 and r1 < ROWS and c1 >= 0 and c1 < COLS
                            and board[r1][c1] == 'O' and (r1, c1) not in visited):
                        q.append((r1, c1))
                        flip.append((r1, c1))
                        visited.add((r, c))
            if not isEdge:
                for r, c in flip:
                    board[r][c] = 'X'

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i, j) not in visited:
                    bfs((i, j))

# Neetcode
# Ok this is a lot nicer, but worst case space complexity is O(n) (when graph is dimension 1xn, the
# call stack becomes depth n) so not really sure why my O(n) space BFS solution was rejected
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(coords):
            r, c = coords
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs((r+1, c))
            dfs((r-1, c))
            dfs((r, c+1))
            dfs((r, c-1))
        
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or i == ROWS-1 or j == 0 or j == COLS-1:
                    dfs((i, j))
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'