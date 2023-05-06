class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if not self.isValidBST(root.left):
            return False

        if root.val <= self.pre:
            return False

        self.pre = root.val

        return self.isValidBST(root.right)



