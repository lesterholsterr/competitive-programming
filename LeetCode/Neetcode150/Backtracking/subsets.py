class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Overall: Had the right idea but could not get the recursion correct
        # Leaps
        # - How can we ensure no elements are repeated? (create the binary tree)
        # - Realize the leaves of the binary tree are exactly what we want to return, so we should
        #   only append to res in the base case

        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res