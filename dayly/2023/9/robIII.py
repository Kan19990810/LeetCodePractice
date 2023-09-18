# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def dfs(st, root):
            if not root:
                return 0
            # 当前节点 抢
            if st:
                return root.val + dfs(False, root.left) + dfs(False, root.right)
            # 当前节点没有抢
            else:
                return max(dfs(True, root.left), dfs(False, root.left)) + max(dfs(True, root.right), dfs(False, root.right))


        return max(dfs(True, root), dfs(False, root))