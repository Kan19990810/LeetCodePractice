class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = [root]

        def dfs(cur, pre, dir):
            if cur.val in to_delete:
                if dir == 'right':
                    pre.right = None
                if dir == 'left':
                    pre.left = None
                if cur.left:
                    dfs(cur.left, cur, 'left')
                if cur.right:
                    dfs(cur.right, cur, 'right')
            else:
                if dir == 'left' and not pre.left:
                    res.append(cur)
                if dir == 'right' and not pre.right:
                    res.append(cur)
                if cur.left:
                    dfs(cur.left, cur, 'left')
                if cur.right:
                    dfs(cur.right, cur, 'right')

        if root.left:
            dfs(root.left, root, 'left')
        if root.right:
            dfs(root.right, root, 'right')
        return res
