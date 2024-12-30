# https://leetcode.com/problems/word-search-ii/
# Observation about DFS that is unrelated to the problem:
# Method 1: Check all directions. Only make DFS calls if valid.
# Method 2: If invalid state, return. Else, make DFS calls in all directions.
# I usually default to method 1, so try to practice method 2 more if possible

# Initial - brute force, TLE
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        brute force: DFS every word - e.g. oath. for every o, see if there is an adjacent a, and so on.
        can be 30000 words though. somehow save previous work?
        e.g. when looking for oath i also found 'oat'
        can have a set to store found words - but these found words would all be prefixes of existing ones
        """
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(board), len(board[0])
        res = []

        # assumes board[x][y] = word[0]
        # updates visited set
        def dfs(word, x, y):
            if len(word) == 1:
                return True
            
            visited.add((x, y))
            for dx, dy in directions:
                if 0 <= x+dx < m and 0 <= y+dy < n and (x+dx, y+dy) not in visited and word[1] == board[x+dx][y+dy]:
                    if dfs(word[1:], x+dx, y+dy):
                        visited.remove((x, y))
                        return True
            visited.remove((x, y))
            return False
        
        def search(word):
            for i in range(m):
                for j in range(n):
                    if word[0] == board[i][j]:
                        if dfs(word, i, j):
                            return True
        
        for word in words:
            if search(word):
                res.append(word)
        
        return res

# Working - instead of DFS for each word, DFS starting from each square. 
# Use a trie to keep track of what words we might find.
# Time complexity is O(m*n*4^10 + l) where l = len(words). Can make this tighter but whatever.
class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(board), len(board[0])
        res = set()

        def dfs(x, y, node, word) -> None:
            if node.isEnd:
                res.add(word)
            
            visited.add((x, y))
            for dx, dy in directions:
                if 0 <= x+dx < m and 0 <= y+dy < n and (x+dx, y+dy) not in visited and board[x+dx][y+dy] in node.children:
                    c = board[x+dx][y+dy]
                    dfs(x+dx, y+dy, node.children[c], word + c)
            visited.remove((x, y))
        
        trie = Node()
        for word in words:
            trie.addWord(word)
        
        # dfs starting from each square
        # visit neighbours if they are in cur.children
        for i in range(m):
            for j in range(n):
                c = board[i][j]
                if c in trie.children:
                    dfs(i, j, trie.children[c], c)
        
        return list(res)
