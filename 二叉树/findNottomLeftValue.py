"""
给定一个二叉树，在树的最后一行找到最左边的值。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -float("INF")
        leftmost_val = 0
        def __traverse(root, cur_depth):
            nonlocal max_depth, leftmost_val
            if not root.left and not root.right:
                if cur_depth > max_depth:
                    max_depth = cur_depth
                    leftmost_val = root.val
            if root.left:
                cur_depth += 1
                __traverse(root.left, cur_depth)
                cur_depth -= 1
            if root.right:
                cur_depth += 1
                __traverse(root.right, cur_depth)
                cur_depth -= 1
        __traverse(root, 0)
        return leftmost_val


from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque()
        if root:
            queue.append(root)
        result = 0
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                if i == 0:
                    result = queue[i].val
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)wwwwwwwwwwwwwwwwwwwwwwwwwwwwwqqqqqqqqqqqqqqqqqqqqq
                if cur.right:
                    queue.append(cur.right)
        return result