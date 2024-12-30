# https://leetcode.com/problems/powx-n/

# Yeah I don't get what they are looking for lol
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

# Binary Exponentiation
# Divide and conquer. 2^10 = 2^5 * 2^5
#                     2^5 = 2^2 * 2^2 * 2
# O(logn) time and memory. Still can do better on memory.
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
        n = abs(n)
        
        def f(i: int):
            if i == 0:
                return 1
            elif i == 1:
                return x
            
            j = f(i // 2)
            if i % 2 == 0:
                return j * j
            return j * j * x
        
        return f(n)
    
# Constant memory
# if power is odd, res *= x
# if power is even, x *= x and power /= 2
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        power = abs(n)

        while power:
            if power % 2 == 0:
                x *= x
                power /= 2
            else:
                res *= x
                power -= 1
        return res if n > 0 else 1/res