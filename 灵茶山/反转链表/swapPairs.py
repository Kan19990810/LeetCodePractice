class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy

        while pre.next and pre.next.next:
            cur = pre.next
            nxt = cur.next

            cur.next = nxt.next
            nxt.next = cur
            pre.next = nxt

            pre = pre.next.next

        return dummy.next




