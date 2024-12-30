# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

# Initial - pretty clear DFS here. Same solution as neetcode :)
class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node('')

    def addWord(self, word: str) -> None:
        cur = self.root
        word += "$"
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]

    def search(self, word: str) -> bool:
        def dfs(node, word):
            if word == "":
                return True
            
            c = word[0]
            if c == '.':
                for child in node.children.values():
                    if dfs(child, word[1:]):
                        return True
                return False
            elif c not in node.children:
                return False
            else:
                return dfs(node.children[c], word[1:])
        
        return dfs(self.root, word + "$")