class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(root, path):
            if root.left is None and root.right is None:
                nonlocal result
                result.append(path)
                return

            path += '->'
            path += str(root.val)

            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)

        dfs(root, '')
        return result

