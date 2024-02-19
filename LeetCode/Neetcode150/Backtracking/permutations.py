# Overall: Obviously brute force is the only way. Challenge was getting the popping and appending
# right in the implementation. As usual, see the base case and build off it.

# Initial Solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(perm, remaining):
            if len(remaining) == 0:
                res.append(perm.copy())
                return

            for i in remaining:
                r_copy = remaining.copy()
                r_copy.remove(i)
                p_copy = perm.copy()
                p_copy.append(i)
                dfs(p_copy, r_copy)

        dfs([], nums)
        return res

# Neetcode way (less copying, iterative)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            res.extend(perms)
            nums.append(n)

        return res
