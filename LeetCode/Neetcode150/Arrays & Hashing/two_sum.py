class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Overall: lol
        # Leaps
        # - We want to SEARCH for numbers and RETURN the index, so the number should be the key and the index should be the value

        seen = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in seen:
                return [seen[x], i]
            else:
                seen[nums[i]] = i
