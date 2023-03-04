"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
"""
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        if not root:
            return results

        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)

        return results

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(root, depth):
            if not root:
                return []
            if len(res) == depth: res.append([])
            res[depth].append(root.val)
            if root.left: helper(root.left, depth + 1)
            if root.right: helper(root.right, depth + 1)
        helper(root, 0)
        return res