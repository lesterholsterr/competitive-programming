class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = nums[0]
        count = 1
        for num in nums:
            if num != cur:
                nums[count] = cur = num
                count += 1
        return count