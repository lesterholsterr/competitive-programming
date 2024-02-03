# Overall: Nothing hard about this problem, just seems like how many style points you can earn.
# Notice a shorter way of iterating through the 9 sub-boxes is to use integer division

# Nice and long so you know it's my solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = [0] * 9

        # Validate rows
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    pass
                elif nums[int(board[i][j]) - 1] != 0:
                    return False
                else:
                    nums[int(board[i][j]) - 1] += 1
            nums = [0] * 9

        # Validate columns
        for i in range(9):
            for j in range(9):
                if board[j][i] == ".":
                    pass
                elif nums[int(board[j][i]) - 1] != 0:
                    return False
                else:
                    nums[int(board[j][i]) - 1] += 1
            nums = [0] * 9

        # Validate sub-boxes
        def isValidSubBox(box):
            nums = [0] * 9
            for i in range(3):
                for j in range(3):
                    if box[i][j] == ".":
                        pass
                    elif nums[int(box[i][j]) - 1] != 0:
                        return False
                    else:
                        nums[int(box[i][j]) - 1] += 1
            return True

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [row[i:i+3] for row in board[j:j+3]]
                if not isValidSubBox(box):
                    return False

        return True

# Neetcode Solution
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[r] or
                    board[r][c] in squares[r // 3, c // 3]):
                    return False
                cols[c].add(board[r][c])
                rows[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True
    
# Even NEATER solution
class Solution:
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                res += [(board[i][j], i), (j, board[i][j]), (board[i][j], i//3, j//3)] # Wow!
        return len(res) == len(set(res))
        