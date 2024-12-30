# https://leetcode.com/problems/missing-number/description/

# Observation here is that a number XOR itself is 0
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        n = len(nums)
        for i in range(n):
            x = x ^ i ^ nums[i]
        x ^= n
        return x