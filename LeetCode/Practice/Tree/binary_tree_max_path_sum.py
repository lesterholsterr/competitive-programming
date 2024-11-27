# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Initial Solution
# Pretty good recursive reasoning
# O(n) time and memory, but only because maxBranch results are being memoized
# The main problem is there are 2 recursive functions, so we are visiting nodes more than once (but still linear)
class Solution:
    def __init__(self):
        self.mb = {}
    
    def maxBranch(self, node: Optional[TreeNode]) -> int:
        # if node is a leaf, max branch = max(0, node.val)
        # otherwise, max branch is either:
        # 1. node.val
        # 2. node.val + maxBranch(node.left)
        # 3. node.val + maxBranch(node.right)
        # 4. 0
        max_branch = 0
        if node:
            if hash(node) in self.mb:
                return self.mb[hash(node)]
            
            max_branch = max(max_branch, node.val)
            if node.left:
                max_branch = max(max_branch, node.val + self.maxBranch(node.left))
            if node.right:
                max_branch = max(max_branch, node.val + self.maxBranch(node.right))
        self.mb[hash(node)] = max_branch
        return max_branch
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # if node is a leaf, max path = the node
        # otherwise, max path is either:
        # 1. Entirely in node.left
        # 2. Entirely in node.right
        # 3. Passes through node (node.val + maxBranch(node.left) + maxBranch(node.right))
        max_path = root.val
        if root.left:
            max_path = max(max_path, self.maxPathSum(root.left))
        if root.right:
            max_path = max(max_path, self.maxPathSum(root.right))
        max_path = max(max_path, root.val + self.maxBranch(root.left) + self.maxBranch(root.right))
        
        return max_path

# Better Solution
# Visit each node once? -> DFS
# Implicitly update the max path once you have the left/right branches of the current node
class Solution:    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = [root.val]

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            max_branch_left = max(0, dfs(root.left))
            max_branch_right = max(0, dfs(root.right))
            
            max_path[0] = max(max_path[0], root.val + max_branch_left + max_branch_right)
            return max(root.val + max_branch_left, root.val + max_branch_right)
        
        dfs(root)
        return max_path[0]
