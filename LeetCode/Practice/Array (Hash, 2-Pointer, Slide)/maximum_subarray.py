class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1: Kadane's, O(n)
        max_sum = nums[0] - 1
        max_so_far = 0
        for num in nums:
            max_so_far += num
            if max_so_far > max_sum:
                max_sum = max_so_far
            if max_so_far < 0:
                max_so_far = 0
        return max_sum

        # Solution 2: Divide and Conquer, O(nlogn)