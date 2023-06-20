class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Overall: Pretty tough problem with a lot of cases to consider. Drawing a visual aid helps a lot here.
        # Leaps
        # - Mid can either be to the left, or right of the pivot. How can we find out which one?
        # - If mid is to the left of pivot, and target is less than mid, then target could be on either side of mid. What do we do here?

        l = 0
        r = len(nums) - 1

        # Condition must be less than OR EQUAL TO!
        # Consider the case where the list contains 1 element
        # Then l = r, but we still need to check the element
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r]:
                # before the pivot
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # after the pivot
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
