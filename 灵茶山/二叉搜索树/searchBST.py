class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = []

        def dfs(root):
            if root is None:
                return

            nonlocal ans
            ans.append(root.val)

            dfs(root.left)
            dfs(root.right)

        while root:
            if root.val > val:
                root = root.left
            elif root.val <val:
                root = root. right
            else:
                dfs(root)
                return ans

        return ans

