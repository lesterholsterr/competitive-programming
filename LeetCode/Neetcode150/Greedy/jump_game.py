# Actual solution is really nice. I ruled out top-down because you can only jump
# forwards and not backwards, turns out you can in fact use top-down by setting
# a "goalpost" and moving it backwards.

# Initial - TLE
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stack = []
        def dfs(i):
            if nums[i] >= len(nums)-i-1:
                return True
            elif nums[i] == 0:
                return False
            
            stack.append((i, nums[i]))
            while stack:
                j, n = stack.pop()
                if n == 0:
                    return False
                elif (dfs(i+n)):
                    return True
                else:
                    stack.append((j, n-1))
            return False
        
        return dfs(0)
    
# Memoized - O(n^2)?
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [-1] * len(nums)
        
        def dfs(i):
            if nums[i] >= len(nums)-i-1:
                return True
            elif nums[i] == 0 or dp[i] == 0:
                return False
            elif dp[i] == 1:
                return True
            
            for j in range(nums[i], -1, -1):
                if dfs(i+j):
                    dp[i+j] = 1
                    return True
                dp[i] = 0
            return False
        
        return dfs(0)

# Neetcode - O(n)!!!!
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            d = goal - i
            if nums[i] >= d:
                goal = i
        
        return True if goal == 0 else False