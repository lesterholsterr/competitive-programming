class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Attempt 1: Got quite close to the solution but was missing one part of it (res variable)

        l = 0
        r = len(nums)-1
        while l < r:
            # If our pointers indicate the subarray is in ascending order, return leftmost element
            if nums[l] <= nums[r]:
                return nums[l]
            
            # Binary search with a twist
            mid = (r-l+1) // 2
            # If our midpoint is greater than first element, then we are in the "bigger" part of the array
            # so we move the left pointer rightwards to get to the "smaller" part
            if nums[mid] > nums[0]:
                l = mid + 1
            # :/ (realized logic doesn't work here)
            else:
                r = mid - 1
        
        # Base Case: If nums is 1, while loop never executes, and we just return the only value
        return nums[l]

        # Solution from https://www.youtube.com/watch?v=nIVW4P8b1VA&t=665s
        l = 0
        r = len(nums)-1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res