# Overall: Not much to see here

# Initial Solution
# Trivial... am I missing something?
# I mean it's O(logn) can't really do much better than that
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        ans = []
        q = collections.deque()
        q.append(root)

        while q:
            l = len(q)
            for i in range(l):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                if i == l-1:
                    ans.append(n.val)

        return ans