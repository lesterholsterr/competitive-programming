# Overall: Pretty straightforward knowing the solution for subsets ii

# Initial Solution
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def solve(i, cur, sum):
            if sum == target:
                ans.append(cur[:])
                return
            elif i >= len(candidates) or sum > target:
                return
            
            cur.append(candidates[i])
            solve(i+1, cur, sum + candidates[i])

            x = 1
            while i+x < len(candidates) and candidates[i] == candidates[i+x]:
                x += 1
            cur.pop()
            solve(i+x, cur, sum)
        
        solve(0, [], 0)
        return ans