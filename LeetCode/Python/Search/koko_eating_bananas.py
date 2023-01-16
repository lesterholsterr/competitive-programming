import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)

        while left <= right:
            k = (left + right) // 2
            
            hours = 0
            for pile in piles:
                hours += math.ceil(1.0 * pile/k)
            
            if hours > h:
                left = k+1
            else:
                right = k-1

        return left