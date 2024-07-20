# So... leetcode really does not want you to use quick select cause they give you test cases that will
# trigger worst case time complexity. Heap solution is trivial to implement anyways, so I still implemented quick select.
import random

class Solution:
    def partition(self, nums, l, r, pivot_index):
        # Hoare partition, constant space
        pivot = nums[pivot_index]
        nums[pivot_index], nums[r] = nums[r], nums[pivot_index] # move pivot to the end
        j = l
        for i in range(l, r):
            if nums[i] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[r], nums[j] = nums[j], nums[r] # restore pivot to correct location
        return j
    
    def findKthLargest(self, nums, k):
        l, r = 0, len(nums) - 1
        while True:
            i = random.randint(l, r) # minimize chance of the worst case
            i = self.partition(nums, l, r, i)
            if i == len(nums) - k:
                return nums[i]
            elif i > len(nums) - k:
                r = i - 1
            else:
                l = i + 1
