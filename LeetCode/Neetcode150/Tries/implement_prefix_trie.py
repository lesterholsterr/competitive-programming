# https://leetcode.com/problems/implement-trie-prefix-tree/description/

# Initial - I know you can do compression but that seems tedious lol
# This is pretty much what neetcode did as well
# yay cs240
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Trie:
    def __init__(self):
        self.root = Node('', {})
        self.root.children['$'] = Node('$', {})

    def insert(self, word: str) -> None:
        cur = self.root
        word += "$"
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c, {})
            cur = cur.children[c]

    def search(self, word: str) -> bool:
        cur = self.root
        word += "$"
        for c in word:
            if not cur or c not in cur.children:
                return False
            cur = cur.children[c]
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not cur or c not in cur.children:
                return False
            cur = cur.children[c]
        return True

