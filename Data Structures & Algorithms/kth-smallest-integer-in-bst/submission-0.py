# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.l = k 
        self.res = None 
        def bruh(root):
            if not root or self.res is not None :
                return

            bruh(root.left)

            self.l -=1 
            if self.l == 0:
                self.res = root.val
                return
            bruh(root.right)

        bruh(root)

        return self.res