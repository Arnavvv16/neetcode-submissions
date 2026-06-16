# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        lol = []
        def idk(node):
            if node is None:
                lol.append(-101)
                return 
            lol.append(node.val)
            idk(node.left)
            idk(node.right)
        idk(p)
        k1 = lol 
        lol = []
        idk(q)
        k2 = lol
        return k1 == k2
