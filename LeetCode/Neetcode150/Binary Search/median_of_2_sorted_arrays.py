# Intuition
# - Notice: The median number of an array means there are an equal number of numbers
#           less than it and greater than it
# - Choose index i for nums1 and index j for nums2. The "left partition" of the
#   combined arry occurs when nums1[i] <= nums2[j+1] and nums2[j] <= nums1[i+1]
#   - I was thinking something along these lines as well
# - If nums1[i] > nums2[j+1], then we have too many numbers from nums1. 
# - Leap: Use binary search on nums1 (note that nums1 must be the shorter of the 2 arrays)
#         to determine index i, then index j will be whatever length is required to complete
#         the left partition
# - The first question to ask yourself is what information do I need to find the median 
#   without merging. The answer is a left partition of the 2 arrays (right also works)

# Initial: Easy linear solution, no way I'm figuring out how to do it in log time
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        if p1 < len(nums1):
            merged += nums1[p1:]
        else:
            merged += nums2[p2:]

        mid = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid] + merged[mid-1]) / 2
        else:
            return merged[mid]

# Neetcode
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        if m+n == 1:
            return nums1[0] if nums1 else nums2[0]

        p = (m+n) // 2
        l, r = 0, m-1
        while True:
            mid1 = (l+r) // 2
            mid2 = p - (mid1 + 1) - 1
            l1 = nums1[mid1] if mid1 >= 0 else float("-inf")
            r1 = nums1[mid1+1] if mid1+1 < m else float("inf")
            l2 = nums2[mid2] if mid2 >= 0 else float("-inf")
            r2 = nums2[mid2+1] if mid2+1 < n else float("inf")

            if l1 > r2:
                r = mid1 - 1
            elif l2 > r1:
                l = mid1 + 1
            elif (m+n) % 2 == 0:  # mistake - used p instead of m+n
                return (max(l1, l2) + min(r1, r2))/2
            else:
                return min(r1, r2)  # mistake: used l1, l2 instead of r1, r2

# Revisited - added commentary
# Why do we want to make n > m? because we calculate mid1 on nums1. This will never be negative.
# Then we calculate mid2 using subtraction. This has the potential to go negative if nums2 is the smaller
# array, but we ensure it is the larger one.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 # <-- invariant: n > m*
        m, n = len(nums1), len(nums2)
        if m+n == 1:
            return nums1[0] if nums1 else nums2[0]
        half = (m+n) // 2
        l, r = 0, m-1
        while True:
            mid1 = (l+r) // 2
            mid2 = half - mid1 - 2 # <-- assumptions: mid1 and mid2 are part of the left partition, n > m
            
            l1 = nums1[mid1] if mid1 >= 0 else float('-inf')
            r1 = nums1[mid1+1] if mid1+1 < m else float('inf')
            l2 = nums2[mid2] if mid2 >= 0 else float('-inf')
            r2 = nums2[mid2+1] if mid2+1 < n else float('inf')
            if l1 > r2:
                r = mid1-1
            elif l2 > r1:
                l = mid1+1
            elif (n+m) % 2 == 1:
                return min(r1, r2)
            else:
                return (max(l1, l2) + min(r1, r2)) / 2