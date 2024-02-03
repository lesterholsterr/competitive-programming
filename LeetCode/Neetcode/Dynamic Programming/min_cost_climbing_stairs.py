# Leaps
# - We don't actually need a 'cache' list, just modify the given list!
# - 

# Initial Solution: Time limit exceeded
# I know the general DP idea but not entirely sure how to code it out
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(cost):
            if len(cost) == 0:
                return 0
            elif len(cost) == 1:
                return cost[0]
            else:
                return cost[0] + min(dfs(cost[1:]), dfs(cost[2:]))
        
        return min(
            cost[0] + dfs(cost[1:]),
            cost[0] + dfs(cost[2:]),
            cost[1] + dfs(cost[2:]),
            cost[1] + dfs(cost[3:]),
        )

# Second Solution: Much better Big O, but bottom 5% of solutions :P
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)

        def dfs(cost, i):
            if len(cost) == 0:
                return 0
            elif len(cost) == 1:
                return cost[0]
            elif cache[i] != -1:
                return cache[i]
            else:
                cache[i] = cost[0] + min(dfs(cost[1:], i+1), dfs(cost[2:], i+2))
                return cache[i]
        
        return min(
            cost[0] + dfs(cost[1:], 1),
            cost[0] + dfs(cost[2:], 2),
            cost[1] + dfs(cost[2:], 2),
            cost[1] + dfs(cost[3:], 3),
        )
    
# Third Solution: Holy shit (hint from Neetcode)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-4, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])