"""
给定一个长度为 n 的链表 head

对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。

返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。如果第 i 个节点没有下一个更大的节点，设置 answer[i] = 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/next-greater-node-in-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = list()
        s = list()
        cur = head
        idx = -1
        while cur:
            idx += 1
            ans.append(0)
            while s and s[-1][0] < cur.val:
                ans[s[-1][1]] = cur.val
                s.pop()
            s.append((cur.val, idx))
            cur = cur.next
        return ans


