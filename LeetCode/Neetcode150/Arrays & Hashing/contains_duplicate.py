class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Overall: Simple
        # Leaps
        # - We want constant lookup but return a boolean value, so a set makes the most sense here

        numset = set()
        for num in nums:
            if num in numset:
                return True
            else:
                numset.add(num)
        return False
