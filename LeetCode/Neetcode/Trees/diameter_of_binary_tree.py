# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Initial Solution - O(n^2) Time
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(n):
            if n is None:
                return 0
            return 1 + max(height(n.left), height(n.right))

        if root is None:
            return 0
        d = height(root.left) + height(root.right)
        return max(d, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    # NeetCode Solution - O(n) time
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            # Now it becomes clear why we made d a list rather than a number
            # d = max(d, l+r+2) would create a new d variable with local scope!
            d[0] = max(d[0], left + right + 2)
            return 1 + max(left, right)

        dfs(root)
        return d[0]

    # Did it by myself again :)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(root):
            if not root:
                return [0, 0]
            hl, dl = dfs(root.left)
            hr, dr = dfs(root.right)
            h = 1 + max(hl, hr)
            d = max(dl, dr, hl+hr)
            return [h, d]

        return dfs(root)[1]
