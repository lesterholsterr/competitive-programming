# Initial Solution
# Well I still remember how to do house robber 1 so basically just solved that question twice here...
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob1, rob2, rob3, rob4 = 0, 0, 0, 0
        for i in range(len(nums)):
            if i != 0:
                rob1, rob2 = rob2, max(rob1 + nums[i], rob2)
            if i != len(nums) - 1:
                rob3, rob4 = rob4, max(rob3 + nums[i], rob4)

        return max(rob2, rob4)

# Ok apparently that was the intended solution. Didn't learn much here :/