class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def getDepth(point, cnt):

            if point is None:
                return

            cnt += 1
            nonlocal ans
            if cnt > len(ans):
                ans.append(point.val)

            getDepth(point.right, cnt)
            getDepth(point.left, cnt)

        getDepth(root, 0)
        return ans