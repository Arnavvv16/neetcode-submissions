class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low=float('-inf'), high=float('inf')):
            # An empty tree/leaf child is technically a valid BST
            if not node:
                return True
            
            # The current node's value must fit strictly within the allowed range
            if not (low < node.val < high):
                return False
            
            # Left child must be < node.val (updates the high boundary)
            # Right child must be > node.val (updates the low boundary)
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root)