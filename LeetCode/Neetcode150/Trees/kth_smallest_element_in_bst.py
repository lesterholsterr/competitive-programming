# Initial - just abused heap
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(n):
            if not n:
                return
            arr.append(n.val)
            dfs(n.left)
            dfs(n.right)
        
        dfs(root)
        heapq.heapify(arr)
        print(arr)
        return heapq.nsmallest(k, arr)[-1]
    
# Redo - oh yeah... I forgot about the BST property
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(n):
            if not n:
                return
            dfs(n.left)
            arr.append(n.val)
            dfs(n.right)
        
        dfs(root)
        return arr[k-1]
    
# Neetcode - cool iterative solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while True: # tree is guaranteed to have k elements
            while cur: # find the smallest node that you haven't visited yet
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop() # take that node out of the stack
            n += 1
            if n == k:
                return cur.val
            cur = cur.right # Otherwise, look on the right subtree
