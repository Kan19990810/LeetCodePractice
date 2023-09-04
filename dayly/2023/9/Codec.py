# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # 后序遍历树，生成字符串
        arr = []
        def postOrder(root:Optional[TreeNode]) -> None:
            if root is None:
                return
            postOrder(root.left)
            postOrder(root.right)
            arr.append(root.val)
        postOrder(root)
        # 数组 int map -> str， join 拼接
        return ' '.join(map(str, arr))
            
        
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        # 二叉搜索树 左节点小于根节点， 右节点大于根节点
        # str 转化为数组
        arr = list(map(int, data.split()))
        def construct(lower:int, upper:int) -> Optional[TreeNode]:
            if arr == [] or arr[-1] < lower or arr[-1] > upper:
                return None
            val = arr.pop()
            root = TreeNode(val)
            root.right = construct(val,upper)
            root.left = construct(lower, val)
            return root
        return construct(-inf ,inf)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans