import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy
        # 将list第一列排序建立堆， 记录下标和数值
        n = len(lists)
        heap = []
        for i in range(n):
            heapq.heappush(heap, {lists[i].val, lists[i]})
        # 当堆中还有数
        while heap:
            # 返回堆顶即最小值
            node = heapq.heappop(heap)
            # 拼接链表
            p.next = node[1]
            p = p.next
            if node[1].next:
                heapq.heappush(heap, {node[1].next.val, node[1].next})

        return dummy.next


            