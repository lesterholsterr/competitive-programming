# Overall: I used bottom-up DP cause it's the only strategy I know. But for this question, that
# means more edge cases and thus a longer program.
# The Neetcode solution found a recursive relation and instead traversed the array from left to right.
# It's important to have an 'accumulator' otherwise be hit with exponential blowup and time out

# Initial Solution
# Can't wait to see how much shorter the Neetcode solution is :|
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        nums[-3] += nums[-1]
        for i in range(len(nums)-4, -1, -1):
            nums[i] += max(nums[i+2], nums[i+3])

        return max(nums[0], nums[1])

# Neetcode Solution
# 5 lines is wild
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2) # [..., n-4, n-3, rob1, rob2, n, n+1, n+2, ...]
            rob1, rob2 = rob2, temp
        return rob2