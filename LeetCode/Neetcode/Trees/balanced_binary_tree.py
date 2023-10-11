# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Overall: Eventually thought of the naive approach but unable to make it more efficient.
    # Leaps
    # - Instead of "checking" from the root down, checking from the leaves up allows us to only visit each node once
    # - To make this work, we need to store heights as well as balanced status -> return type of dfs()
    # - A node is balanced if it's subtrees are balanced AND their heights differ by at most 1

    # Initial Solution (15 minutes)
    # Time: O(n^2) - I think
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def height(root) -> int:
            if root is None:
                return 0
            return 1 + max(height(root.left), height(root.right))

        hl = height(root.left)
        hr = height(root.right)
        return abs(hl - hr) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # Neetcode Solution - Linear time
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            bal = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            h = max(left[1], right[1])
            return [bal, h+1]

        return dfs(root)[0]
