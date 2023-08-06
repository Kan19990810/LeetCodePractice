# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(next=head)
        pre, p0, p1 = dummy, head, head.next

        while p0 and p1:
            pre.next = p1
            nxt = p1.next
            p1.next = p0
            p0.next = nxt
            if nxt:
                pre, p0, p1 = p0, nxt, nxt.next
            else:
                pre, p0= p0, nxt
        
        return dummy.next
