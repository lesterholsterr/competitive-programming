# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
# Good DSU practice. Still some trouble implementing find but I think have a
#   decent intuition of when/how to apply it now

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # & can only make the weight smaller
        # 2 nodes in a component should have the same min weight walk
        # otherwise -1
        # DSU to find all components
        # map unique parents -> & of their edges
        # process queries

        parent = list(range(n))
        def find(x: int) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x]) # <-- messed up this line!
            return parent[x]
        
        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        for e in edges:
            union(e[0], e[1])
        
        components = {} # parent -> bitwise and
        for e in edges:
            p = find(e[0])
            if p in components:
                components[p] &= e[2]
            else:
                components[p] = e[2]

        ans = []
        for q in query:
            p1, p2 = find(q[0]), find(q[1])
            if p1 == p2:
                ans.append(components[p1])
            else:
                ans.append(-1)
        return ans
        