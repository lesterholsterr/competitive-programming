class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0

        sum = 0
        running_sum = []
        for num in nums:
            sum += num
            running_sum.append(sum)
        
        if 0 == sum - running_sum[0]: return 0
        for i in range(1, len(running_sum)):
            if running_sum[i-1] == sum - running_sum[i]:
                return i
        return -1