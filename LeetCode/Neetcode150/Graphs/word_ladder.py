# https://leetcode.com/problems/word-ladder/
# Knowing it was a graph question in advance helped
# Not sure I would have seen that the words can be modelled as an adjacency list, but we'll see
#   how well I can pattern match in the future

# Initial... yeah let's use DFS for shortest path great job Matthew
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        valid = set(wordList)
        adj = {word: [] for word in wordList}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for word in wordList:
            for i in range(len(word)):
                for c in alphabet:
                    if c != word[i]:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in valid:
                            adj[word].append(new_word)
        
        min_path = [float('inf')]
        visited = set()
        def dfs(n: str, path: int) -> None:
            if n == endWord:
                min_path[0] = min(min_path[0], path)
                return
            
            visited.add(n)
            for nei in adj[n]:
                if nei not in visited:
                    dfs(nei, path+1)
        
        dfs(beginWord, 1)
        return min_path[0] if min_path[0] != float('inf') else 0

# BFS (correct)
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        valid = set(wordList)
        adj = {word: [] for word in wordList}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for word in wordList:
            for i in range(len(word)):
                for c in alphabet:
                    if c != word[i]:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in valid:
                            adj[word].append(new_word)
        
        q = deque()
        q.append(beginWord)
        visited = set(beginWord)
        path = 0
        while q:
            l = len(q)
            path += 1
            for _ in range(l):
                word = q.popleft()
                visited.add(word)
                if word == endWord:
                    return path
                for nei in adj[word]:
                    if nei not in visited:
                        q.append(nei)
        return 0