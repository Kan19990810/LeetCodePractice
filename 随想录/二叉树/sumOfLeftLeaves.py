"""
计算给定二叉树的所有左叶子之和。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right)

        cur_left_leaf_val = 0
        if root.left and not root.left.left and not root.left.right:
            cur_left_leaf_val = root.left.val

        return cur_left_leaf_val + left_left_leaves_sum + right_left_leaves_sum

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        stack = []
        if root:
            stack.append(root)
        res = 0
        while stack:
            cur_node = stack.pop()
            if cur_node.left and not cur_node.left.left and not cur_node.left.right:
                res += cur_node.left.val
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        return res