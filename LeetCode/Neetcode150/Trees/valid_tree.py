# wow math239 application - is a graph a tree? check if any vertex is part of a cycle!
# Note the "prev" parameter in DFS so we don't go back to the vertex we just came from.

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        
        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for n in adj[i]:
                if n == prev:
                    continue
                if not dfs(n, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)