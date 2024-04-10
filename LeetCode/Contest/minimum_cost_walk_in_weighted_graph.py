# thoughts
# - first time working with a graph represented as adjacency list, and first time using union find
# - use case of union find is when you have DISJOINT SETS (in this case, graphs that may not be
#   connected to each other)
# - a & b <= min(a, b) - in other words, bitwise and always decreases the value
# - (1<<32)-1 is "infinity" for binary

# O(n) time (worst case) and space where n = len(edges)
# credit: https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/solutions/4985439/python3-union-find-template-explanations/
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = {}
        weight = {}

        def find(x):
            if x not in uf:
                uf[x] = x
                weight[x] = (1<<32)-1
                # ^this number in binary is 32 1's
                # we make it the default value so that it will only keep getting smaller as we &
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(s, e):
            ps = find(s)
            pe = find(e)
            # this merges s into e's set (so the identifier becomes pe)
            uf[ps] = pe
            # therefore it is pe's weight which we want to update
            weight[pe] = weight[ps] & weight[pe]
        
        # for each pair of conected nodes, union them and update the weight of the "root"
        for s, e, w in edges:
            union(s, e)
            root = find(s)
            weight[root] &= w
        
        ans = []
        for s, e in query:
            if find(s) != find(e):
                ans.append(-1)
            elif s == e:
                ans.append(0)
            else:
                ans.append(weight[find(s)])
        return ans