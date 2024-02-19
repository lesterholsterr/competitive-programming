import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        # Overall: Brute force solution easily reducible to binary search. I neglected brute force in favour of trying to find an algorithm, which is why I took longer with this problem.
        # Leaps
        # - What should the starting left and right values be?
        # - What do we do in each case? hours ==, <, > h?

        # Initial Solution (30 minutes)
        # Failing some edge cases :/
        # HINDSIGHT: Reason is because the min k might not occur when hours == h, it could also be that hours < h
        l = 0
        r = max(piles)
        mink = 0
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours == h:
                mink = k
                r = k
                if l == r:
                    break
            elif hours > h:
                l = k + 1
            else:
                r = k - 1
        return mink

        # Neetcode Solution
        l = 1
        r = max(piles)
        res = r  # It's better to set the default value to the max possible value
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:  # we can consolidate the hours = h and hours < h conditions
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
