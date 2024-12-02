# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

# This is a graph problem, not a tree problem. 
# Did not realize until it was over. The lookup table is just an adjacency list
# manager list is just a list of edges in a non-conventional way
# Once this observation is made, implementation becomes clear

from collections import deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        lookup = {i: [] for i in range(n)}
        for i in range(n):
            if manager[i] != -1:
                lookup[manager[i]].append(i)
        
        max_time = 0
        q = deque()
        q.append((headID, 0))
        while q:
            l = len(q)
            for _ in range(l):
                emp, t = q.popleft()
                if not lookup[emp]:
                    max_time = max(max_time, t)
                else:
                    for sub in lookup[emp]:
                        q.append((sub, t + informTime[emp]))
        return max_time