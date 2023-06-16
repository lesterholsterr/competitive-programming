class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            target = -x
            l = i + 1
            r = len(nums) - 1
            while l < r:
                y = nums[l] + nums[r]
                if y == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif y < target:
                    l += 1
                else:
                    r -= 1
        return res
