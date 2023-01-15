# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def depth(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.depth(node.left), self.depth(node.right))
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return self.depth(root)