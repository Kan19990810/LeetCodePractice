class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ma = -inf
        def dfs(root):
            if root is None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            nonlocal ma
            ma = max(ma, l + r + root.val)
            return max(max(l, r) + root.val, 0)
        dfs(root)
        return ma