class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1: Less memory
        class Solution(object):
            def containsDuplicate(self, nums):
                """
                :type nums: List[int]
                :rtype: bool
                """
                if len(nums) < 2: return False
                nums.sort()
                for i in range(len(nums)-1):
                    if nums[i] == nums[i+1]: return True
                return False

        # Solution 2: Less time
        if len(nums) < 2: return False
        appeared = {}
        for num in nums:
            if num in appeared:
                return True
            else:
                appeared[num] = 1
        return False