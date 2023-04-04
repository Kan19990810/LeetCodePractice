class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right =None
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            result.append(root.val)
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return result

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)
            result.append(root.val)
            traversal(root.right)

        traversal(root)
        return result

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)
            traversal(root.right)
            result.append(root.val)

        traversal(root)
        return result