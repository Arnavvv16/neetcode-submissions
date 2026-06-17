# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        lol = {}
        q.append([root,0])
        while q :
            a,b = q.popleft()
            if b not in lol :
                lol[b] = a.val
            if a.right :
                q.append([a.right,b+1])
            if a.left :
                q.append([a.left, b+1])

        for v in (lol.items()):
            res.append(v[1])

        return res


