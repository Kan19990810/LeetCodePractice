"""
给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = 0
        def traversal(curr: TreeNode) -> int:
            nonlocal result
            if not curr: return 2
            left = traversal(curr.left)
            right = traversal(curr.right)
            if left == 2 and right == 2:
                return 0
            elif left == 0 or right ==0:
                result += 1
                return 1
            elif left == 1 or right ==1:
                return 2
        if traversal(root) == 0:
            result += 1
        return result