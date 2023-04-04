"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        r = float("inf")
        def buildaList(root):
            if not root: return None
            if root.left: buildaList(root.left)
            res.append(root.val)
            if root.right: buildaList(root.right)
            return res

        buildaList(root)
        for i in range(len(res) - 1):
            r = min(abs(res[i] - res[i + 1]), r)
        return r

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        cur = root
        pre = None
        result = float("inf")
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre:
                    result = min(result, abs(cur.val - pre.val))
                pre = cur
                cur = cur.right
        return result
