class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 找到入环口
        # 2 (z + x) = z + k(x + y) + x -> z + x = k(x + y) -> z = (k - 1) x + k y

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                a, b = slow, head
                while a != b:
                    a = a.next
                    b = b.next
                return a
        return None
