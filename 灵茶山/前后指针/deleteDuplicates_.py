class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            va = cur.next.val
            if va == cur.next.next.val:
                while cur.next and cur.next.val == va:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
