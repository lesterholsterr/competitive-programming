# https://leetcode.com/problems/partition-equal-subset-sum/description/

# Initial
# - Backtracking solution is fairly obvious
# - But I still needed help seeing that 2 partitions of same sum = 1 partition of sum(nums)/2
# - Otherwise you're handling 3 variables and it's harder to memoize
# - Anyways it's straightforward to turn this into top down DP
from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def f(i: int, s: int) -> bool:
            if s == 0:
                return True
            elif i == len(nums):
                return False
            
            return f(i+1, s-nums[i]) or f(i+1, s)

        if sum(nums) % 2 != 0:
            return False
        else:
            return f(0, sum(nums)/2)

# Bottom Up
# - Didn't see it :(
# - The challenge is that the relation is now different
# - To put it on a 2D matrix, the parameters would have to be index you are at, and sum
#   - Next time, try and at least intuit what the axes represent
# - Then the relation should be familiar... it is just KNAPSACK
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        partition_sum = sum(nums) // 2
        dp = [[False] * (partition_sum + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        if nums[0] <= partition_sum:
            dp[i][nums[0]] = True
        
        for i in range(1, len(nums)):
            for j in range(1, partition_sum + 1):
                if dp[i-1][j] or (j-nums[i] >= 0 and dp[i-1][j-nums[i]]):
                    dp[i][j] = True
        return dp[-1][-1]
    
# O(n) memory
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        ps = s // 2

        if s % 2 != 0:
            return False

        dp = [True] + [False] * ps
        dp_next = dp.copy()
        if nums[0] < ps:
            dp[nums[0]] = True
        
        for i in range(1, len(nums)):
            for j in range(1, ps+1):
                if j - nums[i] >= 0:
                    dp_next[j] = dp[j] or dp[j-nums[i]]
                else:
                    dp_next[j] = dp[j]
            if dp_next[-1]:
                return True
            dp, dp_next = dp_next, dp
        return dp[-1]