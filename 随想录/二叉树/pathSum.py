"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例: 给定如下二叉树，以及目标和 sum = 22，
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traversal(cur_node, remain):
            if not cur_node.left and not cur_node.right:
                if remain == 0:
                    result.append(path[:])
                return
            if cur_node.left:
                path.append(cur_node.left.val)
                traversal(cur_node.left, remain - cur_node.left.val)
                path.pop()
            if cur_node.right:
                path.append(cur_node.right.val)
                traversal(cur_node.right, remain - cur_node.right.val)
                path.pop()

        result, path = [], []
        if not root:
            return []
        path.append(root.val)
        traversal(root, targetSum - root.val)

        return result

from collections import deque
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        que, temp = deque([root]), deque([(root.val, [root.val])])
        result = []
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                value, path = temp.popleft()
                if (not node.left) and (not node.right):
                    if value == targetSum:
                        result.append(path)
                if node.left:
                    que.append(node.left)
                    temp.append((node.left.val + value, path + [node.left.val]))
                if node.right:
                    que.append(node.right)
                    temp.append((node.right.val + value, path + [node.right.val]))
        return result

