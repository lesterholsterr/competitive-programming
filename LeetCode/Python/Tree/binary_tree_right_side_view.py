import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        
        visited = collections.deque()
        visited.append(root)
        res = []

        while visited:
            l = len(visited)
            level = []
            for i in range(l):
                cur = visited.popleft()
                if cur:
                    visited.append(cur.left)
                    visited.append(cur.right)
                    level.append(cur.val)
            if level:
                res.append(level[-1])
        return res