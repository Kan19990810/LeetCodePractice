class Node(object):
    def __init__(self, x = 0):
        self.val = x
        self.next = Node

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
        self.head.next = new.node
        self.size += 1

    def add