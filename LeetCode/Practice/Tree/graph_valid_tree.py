# https://leetcode.com/problems/graph-valid-tree/

# Solution: Defintely not the greatest
# - Forgot easy check at the start for whether len(edges) == n-1.
# - Trouble thinking about whether DFS should return something or not
#   My workaround was the cycle = [False] variable
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        v_edges = set() # stores edges (a, b) - convention: a < b
        v_nodes = set() # stores nodes n
        adj = {i : [] for i in range(n)} # n -> neighbours
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        if n == 1:
            return True
        
        cycle = [False]
        def dfs(i: int) -> None:
            if i in v_nodes:
                cycle[0] = True
                return
            else:
                v_nodes.add(i)
            
            neighbours = adj[i]
            for neighbour in neighbours:
                if i < neighbour:
                    edge = (i, neighbour)
                else:
                    edge = (neighbour, i)
                
                if edge not in v_edges:
                    v_edges.add(edge)
                    dfs(neighbour)
        
        dfs(0)
        return not cycle[0] and len(v_edges) == len(edges) and len(v_nodes) == n
    

# Solution 1: Good use case for union find.
# Intuition: If 2 nodes are already in the same group, but they also share an edge, there must be a cycle
# No DFS/BFS needed, as we can just iterate through edges once
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        parent = list(range(n)) # [0, 1, ..., n-1]
        def find(x):
            return x if parent[x] == x else find(parent[x])
        for e in edges:
            x = find(e[0])
            y = find(e[1])
            if x == y:
                return False
            parent[y] = x
        return len(edges) == n-1
    
# Solution 2: Elegant DFS
# Intuition: Once you check that there are the correct number of edges, DFS just needs to check
#            that every node is connected, which is quite simple.
# What an elegent solution damn
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        neighbours = {i : [] for i in range(n)}
        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        def visit(i):
            for neighbour in neighbours.pop(i, []):
                visit(neighbour)
        
        visit(0)
        return not neighbours