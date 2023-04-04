"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        candidate_list = []

        def __traverse(root: TreeNode) -> None:
            nonlocal candidate_list
            if not root:
                return
            __traverse(root.left)
            candidate_list.append(root.val)
            __traverse(root.right)

        def __is_sorted(nums: list) -> bool:
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:
                    return False
            return True

        __traverse(root)
        res = __is_sorted(candidate_list)

        return res

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        cur_max = -float("INF")
        def __isValidBST(root: TreeNode) -> bool:
            nonlocal cur_max

            if not root:
                return True

            is_left_valid = __isValidBST(root.left)
            if cur_max < root.val:
                cur_max = root.val
            else:
                return False
            is_right_valid = __isValidBST(root.right)
            return is_left_valid and is_right_valid
        return __isValidBST(root)

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        cur = root
        pre = None
        while cur or stack:
             if cur:
                 stack.append(cur)
                 cur = cur.left
             else:
                  cur = stack.pop()
                  if pre and cur.val <= pre.val:
                      return False
                  pre = cur
                  cur = cur.right
        return True