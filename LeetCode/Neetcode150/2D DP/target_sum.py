# https://leetcode.com/problems/target-sum/description/

# Initial
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 2^20 possibilities for backtracking/brute force
        # f(i, sum) -> number of ways to get to target if you're on index i and have sum so far
        # f(n-1, sum) = 1 if sum + nums[-1] or sum - nums[-1] == target, else 0
        # f(n-2, sum) = f(n-1, sum + nums[n-2]) + f(n-1, sum - nums[n-2]))
        # do this for every single sum for every single n
        # 20 * 1000 * 1 = 20000
        # return f(0, 0)
        
        n = len(nums)
        @cache
        def dp(i, sum) -> int:
            if i == n:
                return 1 if sum == target else 0
            
            return dp(i+1, sum+nums[i]) + dp(i+1, sum-nums[i])
        return dp(0, 0)

# Bottom-Up (some help from AI for implementing the offset)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * 2001
        offset = 1000
        dp[offset + target] = 1

        for i in range(n-1, -1, -1):
            dp_next = [0] * 2001
            for j in range(-1000, 1001):
                j += offset
                if j + nums[i] <= 2000:
                    dp_next[j] += dp[j + nums[i]]
                if j - nums[i] >= 0:
                    dp_next[j] += dp[j - nums[i]]
            dp = dp_next
        
        return dp[offset]

# Most optimal
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {0: 1}
        
        for i in range(len(nums)):
            dp_next = {}
            for sum, count in dp.items():
                dp_next[sum + nums[i]] = dp_next.get(sum + nums[i], 0) + count
                dp_next[sum - nums[i]] = dp_next.get(sum - nums[i], 0) + count
            dp = dp_next
        
        return dp.get(target, 0)