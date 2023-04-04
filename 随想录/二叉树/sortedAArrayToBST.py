"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.traversal(nums, 0, len(nums) - 1)
        return root

    def traversal(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None

        mid = left + (right - left) // 2
        mid_root = TreeNode(nums[mid])
        mid_root.left = self.traversal(nums, left, mid - 1)
        mid_root.right = self.traversal(nums, mid + 1, right)

        return mid_root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        root = TreeNode()
        nodeSt = [root]
        leftSt = [0]
        rightSt = [len(nums)]

        while nodeSt:
            node = nodeSt.pop()
            left = leftSt.pop()
            right = rightSt.pop()
            mid = left + (right - left) // 2
            node.val = nums[mid]

            if left < mid:
                node.left = TreeNode()
                nodeSt.append(node.left)
                leftSt.append(left)
                rightSt.append(mid)
            if right > mid:
                node.right = TreeNode()
                nodeSt.append(node.right)
                leftSt.append(mid + 1)
                rightSt.append(right)
        return root