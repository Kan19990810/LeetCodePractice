class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ma = 0
        def dfs(root):
            if root is None:
                return -1
            l = dfs(root.left)
            r = dfs(root.right)
            nonlocal ma
            if root.left and root.val != root.left.val:
                l = -1
            if root.right and root.val != root.right.val:
                r = -1
            ma = max(ma, l + r + 2)
            return max(l, r) + 1
        dfs(root)
        return ma