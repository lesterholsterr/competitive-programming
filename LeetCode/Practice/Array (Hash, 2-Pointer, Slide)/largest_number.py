# https://leetcode.com/problems/largest-number/
# Was able to identify the way you have to sort this pretty quickly, but struggled to realize 
#   I needed to write a comparator.
# Alternative was to repeat each number 10 times and then sort lexicographically
#   but this is not intuitive at all. Would never come up with this in an interview.

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # at every instance, choose the number starting with the largest digit
        # if there's a tie, look at the next digit
        # if one number has no next digit, assume it is the first digit
        def compare(x: str, y: str):
            print(x)
            print(y)
            if x == y:
                return 0
            i = 0
            ans = 0
            while i < len(x) and i < len(y):
                if x[i] < y[i]:
                    return -1
                elif x[i] > y[i]:
                    return 1
                else:
                    i += 1
            
            if len(x) < len(y):
                if x[0] > y[i]:
                    return 1
                else:
                    return -1
            if x[i] > y[0]:
                return 1
            else:
                return -1
            return ans
        
        nums = [str(nums[i]) for i in range(len(nums))]
        nums2 = sorted(nums, key=cmp_to_key(compare))
        return ''.join(reversed(nums2))
