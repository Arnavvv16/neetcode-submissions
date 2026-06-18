# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()
        q.append([root, float("-inf")])

        while q :
            a, maxx = q.popleft()
            if a.val >= maxx :
                res +=1
            if a.left :
                q.append([a.left, max(a.val,maxx)])
            if a.right:
                q.append([a.right, max(a.val,maxx)])
        return res

        

        
        