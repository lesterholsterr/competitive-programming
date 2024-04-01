# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Solution 1
        # def dfs(root):
        #     if root is None:
        #         return True, 0
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     return left[0] and right[0] and abs(left[1] - right[1]) <= 1, \
        #         1 + max(right[1], left[1])
        
        # return dfs(root)[0]

        # Solution 2
        def height(root):
            if root is None: return 0
            
            left = height(root.left)
            right = height(root.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1
        
        return (height(root) >= 0)