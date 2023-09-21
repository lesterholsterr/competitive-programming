# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Overall: Pretty straightforward. I chose depth-first just because I'm more comfortable with recursion. BFS would also work. Only missed the edge case where a node had only 1 child because I thought that wasn't allowed. Remember to confirm these things with interviewer!
    # Leaps
    # - None!

    # Initial Solution (10 minutes)
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root

    def invert(self, n):
        if n is None:
            return n
        n.left, n.right = n.right, n.left
        self.invert(n.left)
        self.invert(n.right)
        return n

    # Neetcode Solution
    # Didn't actually need a helper function!! Not sure how I didn't notice.
    def invertTree(self, root):
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    # My second solution (BFS!)
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = [root]
        while q:
            n = q.pop(0)
            if n is None:
                continue
            q.append(n.left)
            q.append(n.right)
            n.left, n.right = n.right, n.left
        return root
