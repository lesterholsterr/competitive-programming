# thoughts
# - know from personal experience that word searches use brute force dfs
# - using set to track visited spots felt pretty intuitive too
# - time complexity: O(n * m * 4^len(word))

# Initial: I did it!
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        m, n = len(board), len(board[0])

        def search(coords, i):
            if i == len(word):
                return True
            
            visited.add(coords)
            r, c = coords
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                r1, c1 = r + dr, c + dc
                if (r1 >= 0 and r1 < m and c1 >= 0 and c1 < n and
                    board[r1][c1] == word[i] and (r1, c1) not in visited and
                    search((r1, c1), i+1)):
                    return True
            visited.remove(coords)
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and search((i, j), 1):
                    return True
        return False