# The XOR of 2 of the same number is 0. So the XOR of every number in nums is the single number.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
        return ans