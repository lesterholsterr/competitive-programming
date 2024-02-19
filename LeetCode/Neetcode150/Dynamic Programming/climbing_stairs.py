# Overall: Notice the intuition behind the observed Fibonacci pattern. Case n is reduced to case n-1
# and case n-2. There are no duplicate solutions in these cases because your first step differs.
# Therefore climbStairs(n) = climbStairs(n-1) + climbStairs(n-2).
# Reducing a problem to a previously solved state is the essence of DP (I think).

# Initial Solution (this is NOT DP lol)
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0

        for i in range(n//2 + 1):
            # aCb = a! / b!(a-b)!
            a = n-i
            b = i
            ways += math.factorial(a) / (math.factorial(b)
                                         * math.factorial(a-b))

        return int(ways)

    #     n stairs
    #     0 2-steps: 1 way - nC0
    #     1 2-step:  n-1 ways - (n-1)C1
    #     2 2-steps: (n-2)C2
    #     3 2-steps: (n-3)C3

    #             _
    #           _|
    #         _|
    #       _|
    #     _|
    #    |

# DP Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        one, two = 1, 1
        for i in range(n):
            one, two = two, one+two

        return one
