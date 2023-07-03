class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        p0 = res
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        n = self.length(l1)
        m = self.length(l2)
        if m > n:
            l1, l2, n, m = l2, l1, m, n
        i = 0
        if n == m:
            for _ in range(m - 1):
                idx = (l1.val + l2.val + i) // 10
                p0.val = (l1.val + l2.val + i) % 10
                i = idx
                p0.next = ListNode()
                p0 = p0.next
                l1 = l1.next
                l2 = l2.next

            p0.val = (l1.val + l2.val + i) % 10
            if (l1.val + l2.val + i) // 10 == 1:
                p0.next = ListNode(val=1)
                p0 = p0.next
        else:
            for _ in range(m):
                idx = (l1.val + l2.val + i) // 10
                p0.val = (l1.val + l2.val + i) % 10
                i = idx
                p0.next = ListNode()
                p0 = p0.next
                l1 = l1.next
                l2 = l2.next

            for _ in range(n - m - 1):
                idx = (l1.val + i) // 10
                p0.val = (l1.val + i) % 10
                i = idx
                p0.next = ListNode()
                p0 = p0.next
                l1 = l1.next
            p0.val = (l1.val + i) % 10
            if (l1.val + i) // 10 == 1:
                p0.next = ListNode(val=1)
                p0 = p0.next

        return self.reverse(res)

    def reverse(self, l: Optional[ListNode]) -> Optional[ListNode]:

        cur = l
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def length(self, l: Optional[ListNode]) -> int:
        dummy = ListNode(next=l)
        p0 = dummy
        n = 0
        while p0.next:
            n += 1
            p0 = p0.next

        return n
