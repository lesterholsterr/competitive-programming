# https://leetcode.com/problems/ipo/description/?envType=daily-question&envId=2024-06-15

# Initial - actually so proud of my solution, but unfortunately MLE
from functools import cache

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        f(i, k, w) -> given projects[i:], and ability to do up to k projects, and currently w capital, return max profit
        - if i == n or k == 0 or capital[j] < w for all i <= j < n -> 0
        - f(i, k, w) = 
            - if capital[i] <= w (can afford): max(profits[i] + f(i+1, k-1, w+profits[i]), f(i+1, k, w))
            - if capital[i] > w (can't afford): profits(i+1, k, w)
        """
        # k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
        n = len(profits)
        @cache
        def dp(i, k, w) -> int:
            if i == n or k == 0:
                return 0
            
            if capital[i] <= w:
                return max(profits[i] + dp(i+1, k-1, w+profits[i]), dp(i+1, k, w))
            else:
                return dp(i+1, k, w)
        
        return w + dp(0, k, w)

# Ohh it's actually GREEDY!!! Looks so similar to knapsack problem goddamn
# The key distinction is that projects have no COST! Only a COST PREREQUISITE.
# So just choose the best project each time given your cost prerequisite.
from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        arr = [(profits[i], capital[i]) for i in range(n)]
        arr.sort(key=lambda x: x[1])
        heap = []
        i = 0
        for _ in range(k):
            while i < n and arr[i][1] <= w:
                heappush(heap, -arr[i][0])
                i += 1
            if not heap:
                break
            w += -heappop(heap)
        return w