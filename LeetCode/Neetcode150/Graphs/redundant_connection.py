# https://leetcode.com/problems/redundant-connection/

# I need to stop spamming DSU lol
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(x: int) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        for a, b in edges:
            pa, pb = find(a), find(b)
            if pa == pb:
                return [a, b]
            union(a, b)

# DFS just for practice (even though less efficient)
class Solution:
   def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Add 1 edge at a time to my graph until a cycle is created
        # The edge that creates the cycle is a redundant connection
        # Iterate edges[0..n-1] guarantees you return the last one
        n = len(edges)
        adj = {i: [] for i in range(n+1)}

        def dfs(n: int, par: int) -> bool:
            if n in visited:
                return True
            
            visited.add(n)
            for nei in adj[n]:
                if nei != par:
                    if dfs(nei, n):
                        return True
            return False
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            visited = set()
            if dfs(b, None):
                return [a, b]

