class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 计算链表长度
        n = 0
        p = head
        while p:
            p = p.next
            n += 1
        
        # 链表折中， 若长度为奇数，则留长的一半
        if n % 2 == 0:
            n //= 2
        else:
            n = n // 2 + 1

        # 找到后一半的起点
        p = head
        while n > 1:
            p = p.next
            n -= 1        
        nxt = p.next
        p.next = None
        p = nxt


        # 翻转后一半链表
        pre = None
        while p:
            nxt = p.next
            p.next = pre
            pre = p
            p = nxt

        # 拼接前一半链表以及后一半链表
        cur = head
        p = pre
        while cur and p:
            cnxt = cur.next
            pnxt = p.next
            cur.next = p
            cur.next.next = cnxt
            cur = cnxt
            p = pnxt
        
        return head

