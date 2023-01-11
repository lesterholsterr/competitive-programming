class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        n_1, n_2 = 1, 1
        sum = 0
        for i in range(n-1):
            sum = n_1 + n_2
            n_1 = n_2
            n_2 = sum
        return sum