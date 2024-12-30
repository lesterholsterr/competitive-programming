# https://leetcode.com/problems/sum-of-two-integers/

# Initial - I think this works with positive numbers? 
# Negatives mess it up though...
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]
        l = max(len(a), len(b))
        a = a.zfill(l)
        b = b.zfill(l)
        print(a)
        print(b)

        res = 0
        carry = 0
        for i in range(l-1, -1, -1):
            x = int(a[i])
            y = int(b[i])
            z = x ^ y ^ carry
            if z:
                res |= 1 << (l - i - 1)
            if (x and y) or (x and carry) or (y and carry):
                carry = 1
            else:
                carry = 0

        if carry:
            res |= 1 << l
        
        return res

# Neetcode (The algorithm doesn't work as well in Python)
# a ^ b is the sum with no carries
# (a & b) << 1 is the carries
# if there are no carries, the sum is correct
# otherwise, add the sum and carries
# handles negatives due to 2's complement representation
class Solution {
public:
    int getSum(int a, int b) {
        while (b != 0) {
            int tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }
        return a;
    }
};
