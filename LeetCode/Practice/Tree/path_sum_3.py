# https://leetcode.com/problems/path-sum-iii/

# Initial - Doesn't work because of duplicate calls
# Wasn't obvious to me at first but think about lines 16 and 17
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = [0]
        def dfs(n: TreeNode, s: int) -> None:
            if not n:
                return
            if s + n.val == targetSum:
                paths[0] += 1
            
            dfs(n.left, s + n.val)
            dfs(n.right, s + n.val)
            dfs(n.left, 0)
            dfs(n.right, 0)
        
        dfs(root, 0)
        return paths[0]

# Really good editorial explanation
# Think about how you would find the # of subarrays that sum to targetSum
# Using preorder traversal, we can basically do the same thing
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = [0]
        dd = defaultdict(int)

        def dfs(n: TreeNode, s: sum) -> None:
            if not n:
                return
            
            s += n.val
            if s == targetSum:
                paths[0] += 1
            paths[0] += dd[s - targetSum]

            dd[s] += 1
            dfs(n.left, s)
            dfs(n.right, s)
            dd[s] -= 1
        
        dfs(root, 0)
        return paths[0]