class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        if l <= 2: 
            return nums[0]
        
        min = len(nums)//2 + 1
        elems = {}
        for num in nums:
            if num in elems:
                elems[num] += 1
                if elems[num] == min:
                    return num
            else:
                elems[num] = 1