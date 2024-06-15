# Thoughts
# - DP did not feel obvious, it's just a cumulative max and min product
# - I correctly identified 0 as being a "reset" and having to somehow deal with an oscillating cumprod
#   for negative values (although never considered keeping a min product)
# - Have assignments to do, will reflect more at a later time

# Initial - I'm trolling :facepalm:
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        hasZero = True if nums.count(0) > 0 else False
        arr = []
        cumprod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                arr.append(cumprod)
            else:
                cumprod *= nums[i]
        arr.append(cumprod)
        
        ans = max(arr)
        if hasZero:
            ans = max(0, ans)
        if ans < 0:
            ans = min(nums)
        return ans
    
# Neetcode 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            # if n == 0:
            #     curMin, curMax = 1, 1
            #     continue
            
            temp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * temp, n * curMin, n)
            res = max(res, curMax)
        
        return res