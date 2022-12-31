class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Solution 1: O(n^2)
        # if len(nums) == 1: return nums[0]
        # checked = []
        # for num in nums:
        #     if num in checked:
        #         checked.remove(num)
        #     else:
        #         checked.append(num)
        # return checked[0]

        # Solution 2: O(n) time and space
        # Honestly why does this even work
        res = 0
        for num in nums:
            res = res ^ num
        return res