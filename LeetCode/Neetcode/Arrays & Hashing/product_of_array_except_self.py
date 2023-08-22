class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Overall: Good job with implementation and edge cases, but needed a hint to realize the essential concept of prefix/postfix.
        # Leaps
        # - 

        # Initial Solution (20 minutes + hint)
        pre, post, ans = [0] * len(nums), [0] * len(nums), [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                pre[i] = nums[i]
            else:
                pre[i] = pre[i-1] * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                post[i] = nums[i]
            else:
                post[i] = post[i+1] * nums[i]

        for i in range(len(nums)):
            if i == 0:
                ans[i] = post[i+1]
            elif i == len(nums)-1:
                ans[i] = pre[i-1]
            else:
                ans[i] = pre[i-1] * post[i+1]
        return ans
    
        # Neetcode Solution (O(1) memory)
        ans = [1] * len(nums)
        for i in range(len(nums) - 1):
            ans[i + 1] = ans[i] * nums[i]
        
        count = 1
        for i in range(len(nums) - 1, 0, -1):
            count *= nums[i]
            ans[i - 1] *= count
        
        return ans