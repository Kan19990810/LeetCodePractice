class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def sumNumber(root: Optional[TreeNode], cnt: int):
            if root.right is None and root.left is None:
                nonlocal ans
                ans += cnt * 10 + root.val
                return
            cnt = cnt * 10 + root.val
            if root.left is not None:
                sumNumber(root.left, cnt)
            if root.right is not None:
                sumNumber(root.right, cnt)

        sumNumber(root, 0)
        return ans
