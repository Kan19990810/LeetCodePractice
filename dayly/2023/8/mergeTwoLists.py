class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p0 = ListNode()
        head = p0
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val <= p2.val:
                nxt = p1.next
                p1.next = None
                p0.next = p1
                p1 = nxt
                p0 = p0.next
            else:
                nxt = p2.next
                p2.next = None
                p0.next = p2
                p2 = nxt
                p0 = p0.next
        if p1:
            p0.next = p1
        if p2:
            p0.next = p2
        
        return head.next