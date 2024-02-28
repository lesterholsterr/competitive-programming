# Overall: With hashing, there are so many ways to solve this. For an elegant solution, notice that
# the start of a sequence will have no left neighbour.
# This is easier than writing a helper function to "traverse" the set to find the length of the 
# current sequence, which is what I did

# Initial Solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        numset = set(nums)
        
        def search(n):
            numseq = 1
            if n in numset:
                numset.remove(n)
            if n-1 in numset:
                numseq += search(n-1)
            if n+1 in numset:
                numseq += search(n+1)
            return numseq
        
        maxseq = 1
        for n in nums:
            maxseq = max(maxseq, search(n))

        return maxseq
    
# Neetcode Solution
# Pretty sure this is O(n) too, but Leetcode says it's much slower?
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxseq = 0

        for n in nums:
            if n-1 not in numset:
                l = 0
                while n + l in numset:
                    l += 1
                maxseq = max(maxseq, l)

        return maxseq