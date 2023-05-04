class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre, last = dummy, dummy
        for _ in range(n):
            pre = pre.next

        while pre.next:
            pre = pre.next
            last = last.next

        last.next = last.next.next

        return dummy.next
