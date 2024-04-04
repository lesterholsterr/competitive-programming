# thoughts
# - really just testing whether you can turn the rules of a bst into a recursive step
# - basically we must have l < n.val < r, where l and r are adjusted differently
#   depending on whether you look at the left child or right child

# initial: took a while but i got it myself
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(l: int, r: int, n: Optional[TreeNode]) -> bool:
            if not n:
                return True
            return (n.val > l and n.val < r and
                    dfs(l, min(r, n.val), n.left) and
                    dfs(max(l, n.val), r, n.right))

        return dfs(-inf, inf, root)

# neetcode solution is the same. only thing is you don't actually need the min() and max()