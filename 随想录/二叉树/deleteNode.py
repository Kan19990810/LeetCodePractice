"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点； 如果找到了，删除它。 说明： 要求算法时间复杂度为 $O(h)$，h 为树的高度。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left: return root.right
            if not root.right: return root.left
            node = root.right
            while node.left:
                node = node.left
            node.left = root.left
            root = root.right
        return root


class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        p = root
        last = None
        while p:
            if p.val == key:
                if p.right:
                    if p.left:
                        node = p.right
                        while node.left:
                            node = node.left
                        node.left = p.left
                    right = p.right
                else:
                    right = p.left
                if last == None:
                    root = right
                elif last.val > key:
                    last.left = right
                else:
                    last.right = right
                break
            else:
                last = p
                if p.val > key:
                    p = p.left
                else:
                    p = p.right
        return root