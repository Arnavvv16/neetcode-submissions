class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxx = float("-inf")
        
        def dfs(node):
            if not node:
                return 0
            ls = dfs(node.left)
            rs = dfs(node.right)
            ls = max(ls, 0)
            rs = max(rs, 0)
            self.maxx = max(self.maxx, node.val + ls + rs)
            
            return node.val + max(ls, rs)
        
        dfs(root)
        return self.maxx