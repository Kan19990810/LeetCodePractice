class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def depth(root: Optional[TreeNode], cnt: int):
            if root is None:
                return
            cnt += 1
            nonlocal ans
            ans = max(ans, cnt)
            depth(root.left, cnt)
            depth(root.right, cnt)
        depth(root, ans)
        return ans

