# https://leetcode.com/problems/multiply-strings/

# Initial - works, but I think I misunderstood the question and this is actually illegal
# It's also a really dumb solution sooo
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_num(s):
            n = 0
            for c in s:
                d = ord(c) - ord('0')
                n = n * 10 + d
            return n
        
        def num_to_str(n):
            if n == 0:
                return "0"
            
            s = ""
            while n:
                d = n % 10
                n = (n - d) // 10
                s += chr(d + ord('0'))
            return s[::-1]
        
        n1, n2 = str_to_num(num1), str_to_num(num2)
        return num_to_str(n1 * n2)

# Neetcode
# idk this feels like such a weird question
# the observations to make are: 
# - the product has at most len(num1) + len(num2) digits
# - we can represent the number as an array of digits
# now the challenge is figuring out how to write a program for long multiplication
# this solution is quite nice. i don't know how i would have come up with it myself.
# i think i would have calculated each of the intermeidate sums and written a sub-program to
# add strings...
# in the video explanation the intuition is just to "do long multiplication" and see how it
# can be reduced to this repetitive procedure.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                x = int(num1[i]) * int(num2[j])
                res[i + j] += x
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10
        
        res = res[::-1]
        i = 0
        while res[i] == 0:
            i += 1
        res = res[i:]
        return ''.join(map(str, res))