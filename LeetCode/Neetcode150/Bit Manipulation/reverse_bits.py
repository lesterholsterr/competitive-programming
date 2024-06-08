# Shift left (<<) to make number bigger. Shift right (>>) to make it smaller.
# To "extract" a digit from a number, & it with 1. To "write" a digit to 000...0, | it with that number.
# So to reverse, extract a digit from the initial number and then >>. Write that to the new number and then <<.

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            x = n & 1
            n = n >> 1
            ans |= x
            ans = ans << 1
        return ans >> 1
