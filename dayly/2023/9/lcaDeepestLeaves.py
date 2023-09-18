# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 返回高度以及子树里最深公共节点
        def dfs(root):
            if not root:
                return 0, None
            
            d1 , lca1= dfs(root.left)
            d2, lca2 = dfs(root.right)

            if d1 > d2:
                return d1 + 1 , lca1
            if d1 < d2:
                return d2 + 1, lca2
            return d1 + 1, root

        return dfs(root)[1]            
