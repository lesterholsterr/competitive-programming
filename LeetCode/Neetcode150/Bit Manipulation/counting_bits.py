# Easy O(nlogn) solution
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            weight = 0
            while i:
                weight += 1
                i &= i-1
            ans.append(weight)
        return ans

# O(n) solution
# Intuition: Every digit after the leading 1 is a previously solved problem, so 1-D DP.
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        offset = 1

        for i in range(1, n+1):
            if offset << 1 == i:
                offset = offset << 1
            ans.append(1 + ans[i - offset])
        
        return ans