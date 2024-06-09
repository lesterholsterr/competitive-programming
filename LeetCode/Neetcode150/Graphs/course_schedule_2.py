# Overall
# - Topological Sort: Use to order the nodes in a Directed Acyclic Graph (so no cycles)
# such that for every edge u -> v, u comes before v
# Note: Not unique
# - Idea is to create an adjacency list and DFS on each element
# - Since input may have cycles, we need to keep track of visited nodes and return [] if we encounter a cycle

# Initial - had to peek at solution for course schedule 1
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        ans = []
        for i in range(numCourses):
            adj[i] = []
        for a, b in prerequisites:
            adj[a].append(b)
        
        visited = set()
        taken = set()
        def dfs(i):
            if len(adj[i]) == 0: # <-- this is redundant because of the return True in the else statement
                if i not in taken:
                    ans.append(i)
                    taken.add(i)
                return True
            elif i in visited:
                return False
            else:
                visited.add(i)
                prereqs = adj[i]
                for j in prereqs:
                    if not dfs(j):
                        return False
                visited.remove(i)
                adj[i] = [] # <-- if you have a taken set, no need to modify adj in place anymore
                if i not in taken: # <-- redundant
                    ans.append(i)
                    taken.add(i)
                return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans
    
# Neetcode
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle: # Then we have a cycle
                return False 
            if crs in visit: # Already taken this course
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output