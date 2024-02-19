class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Overall: Almost got it first try, missed the edge case of the answer being right next to each other. Quite intuitive two pointer soultion. The justification came naturally.
        # Leaps
        # - Should left and right start at the same or opposite sides? (in other words, will a sliding window help us)
        # - When should left move and when should right move? (It helps if you have a case where moving the wrong one will make you bypass the correct answer)

        # Initial solution (20 minutes)
        l, r = 0, len(height) - 1
        maxsofar = 0

        while l != r:
            maxsofar = max(min(height[l], height[r]) * (r - l), maxsofar)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxsofar
