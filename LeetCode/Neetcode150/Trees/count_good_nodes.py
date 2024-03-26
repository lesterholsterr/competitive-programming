# straightforward dfs not much to see here

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, x):
            if not node:
                return 0
            
            y = 0
            if x <= node.val:
                y += 1
            x = max(x, node.val)
            return y + dfs(node.left, x) + dfs(node.right, x)
        
        return dfs(root, root.val)