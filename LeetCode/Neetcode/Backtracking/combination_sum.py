# Overall: Brute force results in duplicates. The only real challenge is creating a tree that is guaranteed to not give duplicates.
# Leaps
# - If left subtree contains "at least one 2", what must the right subtree contain to guarantee no duplicates?

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combo, sum):
            if sum == target:
                res.append(combo.copy())
                return
            elif sum > target or i == len(candidates):
                return

            combo.append(candidates[i])
            sum += candidates[i]
            dfs(i, combo, sum)

            x = combo.pop()
            sum -= x
            dfs(i+1, combo, sum)

        dfs(0, [], 0)
        return res
