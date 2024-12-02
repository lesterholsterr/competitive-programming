# https://leetcode.com/problems/advantage-shuffle/

# Requirements
# 1. Ensure the *smallest* number in nums1 that is bigger than nums2[i] gets matched with it
# 2. if no valid match, use the smallest number in nums1 as "garbage"

# Intuition: Sort *both* lists
#   - If you sort one, might as well sort the other
#   - You can always adapt the list to "remember" the original index
#   - Now it's easy to satisfy requirement 1 with a 2 POINTER approach
#   - Simple temp list to satisfy requirement 2

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()
        nums2_with_index = [(nums2[i], i) for i in range(n)]
        nums2_with_index.sort()
        res = [0] * n

        j = 0
        temp = []
        for i in range(n):
            x, idx = nums2_with_index[i]
            while j < n and nums1[j] <= x:
                temp.append(nums1[j])
                j += 1
            
            if j == n:
                res[idx] = temp.pop()
            else:
                res[idx] = nums1[j]
                j += 1
        
        return res