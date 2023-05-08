from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = inf
        def dfs(root, pre):
            if root is None:
                return

            dfs(root.left, pre)

            nonlocal ans
            ans = min(root.val - pre, ans)
            pre = root.val

            dfs(root.right, pre)

        dfs(root, 0)
        return ans