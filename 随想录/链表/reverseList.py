# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while(cur != None):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:

        def reverse(pre, cur):
            if not cur:
                return pre

            tmp = cur.next
            cur.next = pre

            return reverse(cur, temp)

    def reverseList3(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        p = self.reverseList3(head.next)
        head.next.next = head
        head.next = None
        return p
