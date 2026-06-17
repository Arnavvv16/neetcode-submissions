# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue =deque([])
        queue.append([root])
        if root is None:
            return []
        output=[[root.val]]
        while(len(queue)!=0):
            a = queue.popleft()
            list1=[]
            list2=[]
            for node in a:
                if node.left is None and node.right is not None:
                    list1.append(node.right)
                    list2.append(node.right.val)
                elif node.right is None and node.left is not None:
                    list1.append(node.left)
                    list2.append(node.left.val)
                elif node.left is None and node.right is None:
                    continue
                
                else:
                    if node.left:   # guard against None
                        list1.append(node.left)
                        list2.append(node.left.val)
                    if node.right:  # guard against None
                        list1.append(node.right)
                        list2.append(node.right.val)
            if len(list1)!=0 and len(list2)!=0:
                output.append(list2)
                queue.append(list1)
        return output