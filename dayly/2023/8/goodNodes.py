class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 递归做
        def dfs(root, ma):
            if root is None:
                return 0
            res = 0
            if root.val >= ma:
                res += 1
                ma = root.val
            res += dfs(root.left, ma) + dfs(root.right, ma)
            return res
        return dfs(root, -inf)
        #     if root.val >= ma:
        #         if not root.right and root.left:
        #             return 1
        #         if root.right and root.left:
        #             return 1 + dfs(root.right, root.val) + dfs(root.left, root.val)
        #         if root.right:
        #             return 1 + dfs(root.right, root.val)
        #         if root.left:
        #             return 1 + dfs(root.left, root.val)
                
        #     else:
        #         if not root.right and not root.left:
        #             return 0
        #         if root.right and root.left:
        #             return dfs(root.right, ma) + dfs(root.left, ma)
        #         if root.right:
        #             return dfs(root.right, ma)
        #         if root.left:
        #             return dfs(root.left, ma)
                
        # ans = dfs(root, -inf)
        # return ans