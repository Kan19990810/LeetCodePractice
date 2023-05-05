class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lDepth = self.minDepth(root.left)
        rDepth = self.minDepth(root.right)
        return min(lDepth, rDepth) + 1 if lDepth > 0 and rDepth > 0 else max(lDepth, rDepth) + 1