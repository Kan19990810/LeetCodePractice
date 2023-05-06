class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if root is None:
                return 0
            if (leftHeight := getHeight(root.left)) == -1:
                return -1
            if (rightHeight := getHeight(root.right)) == -1:
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            return 1 + max(leftHeight, rightHeight)

        return True if getHeight(root) >= 0 else False
