# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 最大公约数 18 2 * 3 * 3 6 2 * 3 
        p = head
        while p and p.next:
            n = self.gcd(p.val, p.next.val)
            nxt = p.next
            p.next = ListNode(val= n, next = nxt)
            p = nxt
        return head

    def gcd(self, a, b):

        if(b == 0):
            return a
        
        return self.gcd(b ,a % b)
    

