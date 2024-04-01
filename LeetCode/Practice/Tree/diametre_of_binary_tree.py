# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Solution inspired by https://leetcode.com/problems/diameter-of-binary-tree/solutions/1515564/python-easy-to-understand-solution-w-explanation/?languageTags=python
    
    def __init__(self):
        self.diametre = 0

    def depth(self, n):
        if n.left:
            left = self.depth(n.left)
        else:
            left = 0
        if n.right:
            right = self.depth(n.right)
        else:
            right = 0
        if left + right > self.diametre:
            self.diametre = left + right
        
        if left > right:
            return 1 + left
        else:
            return 1 + right
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth(root)
        return self.diametre