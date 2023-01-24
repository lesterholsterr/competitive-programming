class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution 1: O(n^2)
        for i in range(len(nums)):
            x = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == x:
                    return [i, j]

        # Solution 2: O(n)
        vals = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in vals:
                return [i, vals[x]]
            else:
                vals[nums[i]] = i