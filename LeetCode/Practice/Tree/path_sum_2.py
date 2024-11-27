# https://leetcode.com/problems/path-sum-ii/
# Easy DFS
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = [] # 
        cur = [] # [5, 4, 11, 7]
        cur_sum = [0] # [27, 22, 18, 7]

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            cur.append(node.val)
            cur_sum[0] += node.val
            if not node.left and not node.right:
                if cur_sum[0] == targetSum:
                    ans.append(cur.copy())
            else:
                dfs(node.left)
                dfs(node.right)
            cur_sum[0] -= cur.pop()
        
        dfs(root)
        return ans