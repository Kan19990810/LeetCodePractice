"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？
"""
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next = head)
        slow, fast = dummy, dummy
        while(n != 0):
            fast = fast.next
            n -= 1
        while(fast.next!= None):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next