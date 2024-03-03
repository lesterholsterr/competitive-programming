# Overall: Having done Subsets 1, really should have figured this out myself. 
# The thought process is the same: 2 recursive calls, one that includes X and another
# that does not. Just adjust it so that ALL X are excluded.

# Initial soluiton: O(2^n * nlogn) yikes
# Behaving unexpectedly for some test cases and can't debug
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []
        dupeset = set()


        def dfs(nums):
            if len(nums) == 0:
                if not dupeSet(cur):
                    res.append(cur.copy())
                return
            cur.append(nums[0])
            dfs(nums[1:])
            cur.pop()
            dfs(nums[1:])
        
        def dupeSet(s):
            s.sort()
            t = tuple(s)
            if t in dupeset:
                return True
            else:
                dupeset.add(t)
                return False
        
        dfs(nums)
        return res
    
# Neetcode Solution
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res