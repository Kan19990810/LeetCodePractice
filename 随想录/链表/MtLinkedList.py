class Node(object):
    def __init__(self, x = 0):
        self.val = x
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        while(index):
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)
        cur = self.head
        while(cur.next):
            cur = cur.next
        cur.next = new_node
        self.size += 1
    def addAtIndex(self, index, val):
        if index < 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return

        node = Node(val)
        pre = self.head
        while(index):
            pre = pre.next
            index -= 1
        node.next = pre.next
        pre.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        pre = self.head
        while(index):
            pre = pre.next
            index -= 1
        pre.next = pre.next.next
        self.size -= 1


