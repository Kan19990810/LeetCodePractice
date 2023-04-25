class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        low, fast = head, head

        while fast and fast.next:
            low = low.next
            fast = fast.next.next
            if low == fast:
                return True

        return False
