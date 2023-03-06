"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.get_height(root) != -1:
            return True
        else:
            return False

    def get_height(self, root: TreeNode) -> int:
        if not root:
            return 0
        if(left_height := self.get_height(root.left)) == -1:
            return -1
        if(right_height := self.get_height(root.right)) == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)

class Solution:
    def isBalance(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        height_map = {}
        stack = [root]
        while stack:
            node =stack.pop()
            if node:
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            else:
                real_node = stack.pop()
                left, right = height_map.get(real_node.left, 0), height_map(real_node.right, 0)
                if abs(left - right) > 1:
                    return False
                height_map[real_node] = 1 + max(left,right)
        return True