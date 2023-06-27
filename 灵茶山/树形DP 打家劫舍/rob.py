class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            lRob, lNotRob = dfs(node.left)
            rRob, rNotRob = dfs(node.right)
            rob = node.val + lNotRob + rNotRob
            notRob = max(lRob, lNotRob) + max(rRob, rNotRob)
            return rob, notRob
        return max(dfs(root))