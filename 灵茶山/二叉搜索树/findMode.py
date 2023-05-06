class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        orderList = []
        def orderroot(root):
            if not root:
                return

            orderroot(root.left)

            nonlocal orderList
            orderList.append(root.val)

            orderroot(root.right)

        orderroot(root)

        ans = []
        ma = 0
        num = Counter()

        for _, element in enumerate(orderList):
            num['element'] += 1
            if num['element'] > ma:
                ans = [element]
                ma = num['element']
            elif num['element'] == ma:
                ans.append(element)

        return ans



