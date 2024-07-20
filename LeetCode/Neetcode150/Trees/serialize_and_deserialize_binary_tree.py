# DFS approach, could try BFS approach later

# Initial
import math
import ast

class Codec:
    def maxIndex(self, root, index):
        if not root:
            return max(0, math.ceil((index-1)/2))
        return max(self.maxIndex(root.left, index*2+1),
                   self.maxIndex(root.right, index*2+2))

    def makeList(self, root):
        if not root:
            return []
        i = self.maxIndex(root, 0)
        return [None] * i
    
    def dfs(self, root, arr, index):
        if not root:
            return
        arr[index] = root.val
        self.dfs(root.left, arr, index*2+1)
        self.dfs(root.right, arr, index*2+2)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        arr = self.makeList(root)
        self.dfs(root, arr, 0)
        return str(arr)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = ast.literal_eval(data)
        for i in range(len(arr)): # I GENUINELY DO NOT KNOW WHY THIS WORKS
            print(arr[i])
        print(arr[0]) # BUT THIS DOES NOT WORK

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Neetcode
import math
import ast

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(n):
            if not n:
                res.append("N")
                return
            res.append(str(n.val))
            dfs(n.left)
            dfs(n.right)
        
        dfs(root)
        return ",".join(res)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0 # global variable

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            n = TreeNode(int(vals[self.i]))
            self.i += 1
            n.left = dfs()
            n.right = dfs()
            return n

        return dfs()
