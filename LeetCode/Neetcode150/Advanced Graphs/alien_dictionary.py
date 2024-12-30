# https://leetcode.com/problems/alien-dictionary/

# Initial
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        from starting letters: w > e > r
        from 1 and 2: t > f
        from 3 and 4: r > t
        by transitivity: wertf
        we can represent each letter as a node in a DAG
        each node has edges pointing to things it is bigger than
        somehow resolve cycles? (this should be deterministic)
        if there are no disconnected nodes, we have a complete lexical ordering
        """
        letters = {c for s in words for c in s}
        adj = {c: [] for c in letters}
        # don't really think I can implement this


# Solution - good train of thought, but I completely forgot topological sort
# Topological Sort
# - Use case: Finding "prerequisites" in a DAG
# - Analogy: Post-order DFS
# We implemented using DFS here. But there is also Kahn's Algorithm (future learning)
# Definitely need more practice with implementation
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        letters = {}
        adj = {c: set() for w in words for c in w}

        # Build graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            l = min(len(w1), len(w2))
            if w1[:l] == w2[:l] and len(w1) > len(w2): # 'abc' cannot come before 'ab'
                return ""
            for j in range(l):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        # Topo sort
        visit = {} # True = already "locked in"
        res = []

        def dfs(c):
            if c in visit:
                return visit[c] # True = "currently visiting", False = "already visited"
            
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei): # If "currently visiting" and we visit it again, cycle detected
                    return True
            visit[c] = False
            res.append(c) # append at the end because post-order DFS

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return ''.join(res)
