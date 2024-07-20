# Initial - got it :)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        emptyRow = "." * n
        board = [emptyRow] * n
        ans = []

        def legal(board, x, y):
            # check row
            for i in range(n):
                if i == x:
                    continue
                elif board[i][y] == "Q":
                    return False
            
            # check column
            for j in range(n):
                if j == y:
                    continue
                elif board[x][y] == "Q":
                    return False
            
            # check diagonals
            offsets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dx, dy in offsets:
                i, j = x+dx, y+dy
                while (0 <= i and i < n and 0 <= j and j < n):
                    if board[i][j] == "Q":
                        return False
                    i += dx
                    j += dy
            return True
        
        def bt(r):
            if r == n:
                ans.append(board.copy())
                return
            for i in range(n):
                if legal(board, r, i):
                    board[r] = board[r][:i] + "Q" + board[r][i+1:]
                    bt(r+1)
                    board[r] = board[r][:i] + "." + board[r][i+1:]

        bt(0)
        return ans

# Neetcode
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # Idea: r+c will give you distinct numbers for each bottom-left to top-right diagonal
        negDiag = set() # Same idea for r-c with diagonals going the other direction

        res = []
        board = [["."] * n for i in range(n)]

        def bt(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                bt(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        bt(0)
        return res