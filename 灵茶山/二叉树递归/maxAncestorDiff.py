class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, mi, ma):
            if root is None:
                return 0
            diff = max(abs(root.val - mi), abs(root.val - ma))
            mi = min(mi, root.val)
            ma = max(ma, root.val)

            diff = min(diff, dfs(root.left, mi, ma))
            diff = max(diff, dfs(root.right, mi, ma))
            return diff
        return dfs(root, root.val, root.val)