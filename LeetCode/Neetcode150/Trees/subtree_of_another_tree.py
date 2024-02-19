# Overall: The brute force solution is basically as good as it gets here. I wasted a lot of time trying to not make a helper function, and then even more time debugging recursion logic.
# Leaps
# - There are not 1 but 2 recursive cases. What are they?

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(s, t):
            if not s and not t:
                return True
            elif s and t and s.val == t.val:
                return sameTree(s.left, t.left) and sameTree(s.right, t.right)
            else:
                return False

        if not subRoot:
            return True
        elif not root:
            return False
        elif sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
