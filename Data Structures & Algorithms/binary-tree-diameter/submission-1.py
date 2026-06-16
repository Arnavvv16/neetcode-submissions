# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if curr == None :
                return 0
            k = dfs(curr.left)
            l = dfs(curr.right)
            self.res = max(self.res, k+l)
            return 1 + max(k,l)

        dfs(root)
        return self.res