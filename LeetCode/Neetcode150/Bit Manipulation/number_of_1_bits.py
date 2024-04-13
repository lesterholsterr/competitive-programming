# Solution 1
# Intuition: An odd number in binary must end in a 1 (and even end in 0).
class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n:
            weight += n % 2
            n = n >> 1
        return weight

# Solution 2
# Inituition: n-1 will turn the rightmost 1 into a 0, and the 0s to the right of that into 1s
# So n & n-1 gets rid of that rightmost 1 but also turns those new 1s back into 0s
class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n:
            weight += 1
            n &= n-1
        return weight