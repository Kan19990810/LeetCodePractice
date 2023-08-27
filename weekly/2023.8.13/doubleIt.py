class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 翻转 -> 乘 -> 翻转
        # 非空，不需要虚拟
        pre, cur = head, head.next
        pre.next = None
        # 翻转
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        p = pre
        idx = 0
        # 乘
        while p:
            value = (p.val * 2 + idx) % 10
            idx = (p.val * 2 + idx) // 10
            p.val = value
            pre_p = p
            p = p.next
        
        if idx == 1:
            pre_p.next = ListNode(val=1)

        cur = pre.next
        pre.next = None
        #翻转
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre
