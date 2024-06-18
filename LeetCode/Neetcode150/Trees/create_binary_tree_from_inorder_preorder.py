# Confused preorder with BFS. The examples that Leetcode gave lowkey confused me. 
# Notice 2 facts: 
# 1. root = preorder[0]. 
# 2. The index of root in inorder splits that list into a left and right subtree.
# Now find a recurrence relation.

# Initial - This is me trying to solve the problem thinking preorder is BFS :facepalm:
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder[0] = root
        # everything to the left of preorder[0] in inorder is the left subtree
        # base case: if inorder is empty, return. if inorder is length 1, add a node and return
        print(preorder)
        print(inorder)
        if len(inorder) == 0:
            return
        elif len(inorder) == 1:
            return TreeNode(preorder[0])
        
        rootval = preorder[0]
        inorder_index = inorder.index(rootval)
        preorder_left = preorder[1:]
        inorder_left = inorder[:inorder_index]
        preorder_right = preorder[2:]
        inorder_right = inorder[inorder_index+1:]
        root = TreeNode(rootval)
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root

# Neetcode
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        
        rootval = preorder[0]
        inorder_index = inorder.index(rootval)
        root = TreeNode(rootval)
        root.left = self.buildTree(preorder[1:inorder_index+1], inorder[:inorder_index])
        root.right = self.buildTree(preorder[inorder_index+1:], inorder[inorder_index+1:])
        return root