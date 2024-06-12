# Overall: Got it myself! Just have to find the recursive relation
# Failed a number of edge cases, highlighted below. 

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsofar = [root.val]
        def dfs(n):
            if not n:
                return [0, -inf] # <-- Case when tree is a single negative node
            l, ml = dfs(n.left)
            r, mr = dfs(n.right)
            maxthis = max(ml, mr, l+n.val, r+n.val, l+r+n.val, n.val)
            maxsofar[0] = max(maxsofar[0], maxthis)
            return [max(l, r, 0)+n.val, maxthis] # <- max(l, r, 0) <-- Case when max left or right path are both negative
        
        dfs(root)
        return maxsofar[0]

# Neetcode - Same time complexity but much better. I didn't need 2 return values because 
# maxsofar was anyways being updated as a side effect
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsofar = [root.val]
        
        def dfs(n):
            if not n:
                return 0
            
            l = max(0, dfs(n.left)) # l and r return 0 rather than negative
            r = max(0, dfs(n.right)) 
            maxsofar[0] = max(maxsofar[0], n.val+l+r) # <- which makes this max() have much less cases
            return n.val + max(l, r)
        
        dfs(root)
        return maxsofar[0]