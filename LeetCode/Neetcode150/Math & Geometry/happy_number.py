# Not much to say. Reminds me of Collatz conjecture.
# Idea to check for repeats came pretty naturally.
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)

        while True:
            digits = []
            while n > 0:
                digits.append(n % 10)
                n -= n % 10
                n /= 10
            for d in digits:
                n += d**2
            if n == 1:
                return True
            elif n in seen:
                return False
            seen.add(n)
