"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:  给定如下二叉树，以及目标和 sum = 22，
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def isornot(root, targetsum) -> bool:
            if (not root.left) and (not root.right) and targetsum == 0:
                return True
            if (not root.left) and (not root.right):
                return False
            if root.left:
                targetsum -= root.left.val
                if isornot(root.left, targetsum): return True
                targetsum += root.left.val
            if root.right:
                targetsum -= root.right.val
                if isornot(root.right, targetsum): return True
                targetsum += root.right.val
            return False
        if not root:
            return False
        else:
            return isornot(root, targetSum - root.val)


class Solution:
    def haspathsum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        stack = []
        stack.append((root, root.val))
        while stack:
            cur_node, path_sum = stack.pop()
            if not cur_node.left and not cur_node.right and path_sum == targetSum:
                return True
            if cur_node.right:
                stack.append((cur_node.right, path_sum + cur_node.right.val))
            if cur_node.left:
                stack.append((cur_node.left, path_sum + cur_node.left.val))
        return False

