class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return 
        ans = TreeNode()
        def dfs(root1, root2, ans):
            if not root1 and not root2:
                return 
            
            if root1 and root2:
                ans.val = root1.val + root2.val
                if root1.left or root2.left:
                    ans.left = TreeNode()
                    dfs(root1.left, root2.left, ans.left)
                if root1.right or root2.right:
                    ans.right = TreeNode()
                    dfs(root1.right, root2.right, ans.right)
                
            elif root1:
                ans.val = root1.val
                if root1.left:
                    ans.left = TreeNode()
                    dfs(root1.left, None, ans.left)
                if root1.right:
                    ans.right = TreeNode()
                    dfs(root1.right, None, ans.right)
            
            else:
                ans.val = root2.val
                if root2.left:
                    ans.left = TreeNode()
                    dfs(None, root2.left, ans.left)
                if root2.right:
                    ans.right = TreeNode()
                    dfs(None, root2.right, ans.right)

        dfs(root1, root2, ans)
        return ans

            

