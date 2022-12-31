class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1, O(n^2)
        # checked = []
        # for num in nums:
        #     if num in checked:
        #         return True
        #     else:
        #         checked.append(num)
        # return False

        # Solution 2, O(nlogn)
        if len(nums) < 2: return False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: return True
        return False