class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        first, second = head, head.next
        while first != second:
            if not second or not second.next:
                return False
            second = second.next.next
            first = first.next

        return True