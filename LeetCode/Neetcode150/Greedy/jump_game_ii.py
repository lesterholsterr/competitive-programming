# Overall: 
# - Ok so far these problems under the "Greedy" section look a bit different
# - Themes: single pass, always do the thing that gets you closest to the desired end state

# Initial: O(n^2) DP solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[-1] = 0

        for i in range(n-2, -1, -1):
            x = nums[i]
            for j in range(1, x+1):
                if i+j >= n:
                    break
                dp[i] = min(dp[i+j]+1, dp[i])
        return dp[0]

# Neetcode: O(n) Greedy solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        n = len(nums)
        l, r = 0, 0

        while r < n-1:
            next = 0
            for i in range(l, r+1):
                j = nums[i]
                next = max(next, i+j)
            l = r+1
            r = next
            jumps += 1

        return jumps