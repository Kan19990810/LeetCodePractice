class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        orderList = []
        ans = root.val
        ma = 0
        def orderroot(root):
            if not root:
                return

            orderroot(root.left)

            nonlocal orderList
            orderList.append(root.val)

            orderroot(root.right)

        orderroot(root)

        for idx, element in enumerate(orderList):

