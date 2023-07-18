class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            # 叶子节点， 需要操作为0， 提供金币 root.val - 1
            if root.left is None and root.right is None:
                return 0, root.val - 1

            ans, n = 0, root.val
            # 左子树， 左子树提供的金币 num, 增加的操作 operate + abs(num)
            if root.left:
                operate, num = dfs(root.left)
                ans += operate
                ans += abs(num)
                n += num
            # 右子树， 需要分配给右子树的金币 num， 增加的操作 operate + abs(nums)
            if root.right:
                operate, num = dfs(root.right)
                ans += operate
                ans += abs(num)
                n += num
            # 自己需要有 1 个 金币， 提供 n - 1个金币
            return ans, n - 1

        ans, _ = dfs(root)
        return ans
