# Overall: Simple BFS review. 
# Trick for level order traversal: Use an inner for loop that runs len(q) times.

# Initial Solution
# Doesn't work. For some reason this_lvl keeps containing Nones and I can't figure out why
# Update: Wow ok it was literally just the edge case of [] tripping it up. This solution works too.
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, cur_vals, this_lvl, next_lvl = [], [], [], []
        this_lvl.append(root)

        while True:
            for n in this_lvl:
                cur_vals.append(n.val)
                if n.left:
                    next_lvl.append(n.left)
                if n.right:
                    next_lvl.append(n.right)
            res.append(cur_vals.copy())
            cur_vals = []
            if len(next_lvl) == 0:
                return res
            this_lvl = next_lvl.copy()
            next_lvl = []

# Neetcode Solution
# Ok using the queue's length is definitely more elegant
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            lvl = []
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    lvl.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if lvl:
                res.append(lvl.copy())

        return res
