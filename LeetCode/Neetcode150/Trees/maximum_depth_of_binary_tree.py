# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # Initial Solution (10 minutes)
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.dig(root, 1)

    def dig(self, n, d):
        if n.left is None:
            l = d
        else:
            l = self.dig(n.left, d+1)

        if n.right is None:
            r = d
        else:
            r = self.dig(n.right, d+1)

        return max(l, r)

    # NeetCode: Recursive DFS
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    
