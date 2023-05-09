from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = []
        q = deque([root])
        while q:
            val = []
            for _ in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            ans.append(val)

        return ans[-1][-1]
