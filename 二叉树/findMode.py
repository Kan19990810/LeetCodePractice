"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right                                                                                                                                +++++++++

class Solution:
    def __init__(self):
        self.pre = TreeNode
        self.count = 0
        self.max_count = 0
        self.result = []
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        self.search_BST(root)
        return self.result

    def search_BST(self, cur: TreeNode) -> None:
        if not cur:
            return None
        self.search_BST(cur.left)
        if not self.pre:
            self.count = 1
        elif self.pre.val == cur.val:
            self.count += 1
        else:
            self.count = 1
        self.pre = cur

        if self.count == self.max_count:
            self.result.append(cur.val)
        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [cur.val]

        self.search_BST(cur.right)

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        stack = []
        cur = root
        pre = None
        maxCount, count = 0, 0
        res = []
        while cur or stack:
            if cur:
                 stack.append(cur)
                 cur= cur.left
            else:
                cur = stack.pop()
                if pre == None:
                    count = 1
                elif pre.val == cur.val:
                    count += 1
                else:
                    count = 1
                if count == maxCount:
                    res.append(cur.val)
                if count > maxCount:
                    maxCount = count
                    res.clear()
                    res.append(cur.val)
                pre = cur
                cur = cur.right
        return res
