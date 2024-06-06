# First time using adjacency lists (I think?)
# Main idea here is running DFS on each node in the list, while modifying the list each time
# We are "AND"ing things together, so short circuit and return immediately whever there's a False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = set()
        def dfs(i):
            if len(adj[i]) == 0:
                return True
            elif i in visited:
                return False
            
            visited.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            visited.remove(i)
            adj[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True