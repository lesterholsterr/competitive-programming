# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        inverted = Node()
        inverted.val = root.val
        if root.right != None:
            inverted.left = self.invertTree(root.right)
        if root.left != None:
            inverted.right = self.invertTree(root.left)

        return inverted