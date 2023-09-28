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