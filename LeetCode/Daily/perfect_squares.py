# Initial Solution - brute force, way too slow (sqrt(n)^n time I think :skull:)
class Solution:
    def numSquares(self, n: int) -> int:
        ans = 10000

        def greedy(n, i):
            if n == 0:
                return 0
            if i**2 > n:
                return greedy(n, i-1)
            return 1 + greedy(n - i**2, i)
        
        for i in range(int(n**0.5), 0, -1):
            ans = min(ans, greedy(n, i))

        return ans

# DP (peeked at a solution)
# This seems fairly intuitive except for the fact that you need to fill out index 0 and 1
class Solution:
    def numSquares(self, n: int) -> int:
        solutions = [10000] * (n+1)
        squares = []
        for i in range(1, int(n**0.5)+1):
            squares.append(i**2)
        
        solutions[0] = 0
        solutions[1] = 1
        for i in range(2, n+1):
            for s in squares:
                if s == i:
                    solutions[i] = 1
                elif s < i:
                    solutions[i] = min(solutions[i], solutions[i-s] + solutions[s])
        
        return solutions[-1]