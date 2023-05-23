class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(root, su):
            su += root.val
            if not root.left and not root.right:
                return su >= limit

            if root.left and not dfs(root.left, su):
                root.left = None
            if root.right and not dfs(root.right, su):
                root.right = None

            if root.left or root.right:
                return True
            return False

        if not dfs(root, 0):
            return None
        return root
