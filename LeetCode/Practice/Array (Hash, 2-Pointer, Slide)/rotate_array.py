class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == len(nums): return nums
        while k > len(nums):
            k -= len(nums)
        lastk = nums[len(nums)-k:]
        
        for i in range(len(nums)-k-1, -1, -1):
            nums[i+k] = nums[i]
        for j in range(len(lastk)):
            nums[j] = lastk[j]