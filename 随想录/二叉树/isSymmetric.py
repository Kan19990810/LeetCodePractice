class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left ==None and right == None: return True
        elif left.val != right.val:return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        isSame = outside and inside
        return isSame

import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode:
                continue

            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False

            queue.append(leftNode.left)
            queue.append(rightNode.right)
            queue.append(leftNode.right)
            queue.append(rightNode.left)
        return True

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        que = [root]
        while que:
            this_level_length = len(que)
            for i in range(this_level_length // 2):
                if(not que[i] and que[this_level_length - i - 1]) or (que[i] and not que[this_level_length - 1 - i]):
                    return False
                if que[i] and que[i].val != que[this_level_length - 1 - i].val:
                    return False
            for i in range(this_level_length):
                if not que[i]: continue
                que.append(que[i].left)
                que.append(que[i].right)
            que = que[this_level_length]
        return True