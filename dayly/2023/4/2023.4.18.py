

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                st.append(node) #中
                st.append(None)

                if node.right: #右
                    st.append(node.right)
                if node.left: #左
                    st.append(node.left)
            else:
                node = st.pop()
                result.append(node.val)
        return result
"""
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, mi, ma):
            if root == None:
                return 0
            diff = max(abs(root.val - mi), abs(root.val - ma))
            mi = min(mi, root.val)
            ma = max(ma, root.val)

            diff = max(diff, dfs(root.left, mi, ma))
            diff = max(diff, dfs(root.right, mi, ma))
            return diff
        return dfs(root, root.val, root.val)


