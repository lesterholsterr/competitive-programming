class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Overall: Having done Search in Rotated Sorted Array, this was pretty straightforward. Initial solution failed to account for case where array has length 1, but otherwise good.
        # Leaps
        # - How do we find out whether min is to the left or right of mid? (Consider endpoints)
        # - Which 2 cases should you stop searching?

        # Initial Solution (15 minutes)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[l] <= nums[r]:  # Changed this from < to <= to account for len = 1 case
                return nums[l]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
