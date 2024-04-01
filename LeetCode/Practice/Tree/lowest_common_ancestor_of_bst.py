# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        big = max(p.val, q.val)
        small = min(p.val, q.val)
        r = root.val

        if big < r:
            return self.lowestCommonAncestor(root.left, p, q)
        elif small > r:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root