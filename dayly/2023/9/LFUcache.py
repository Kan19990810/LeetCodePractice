import collections
class Node:
    def __init__(self, key, val, pre= None, nex = None, freq = 0):
        self.pre = pre
        self.nex = nex
        self.freq = freq
        self.val = val
        self.key = key

    def insert(self, nex):
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex


def create_linked_list():
    # 构建一个队列
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head
    return (head, tail)

class LFUCache:

    def __init__(self, capacity: int):
        # 双哈希映射
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        # 检测频率和时间 ：超出容量删除
        self.freaMap = collections.defaultdict(create_linked_list)
        # key -> node  ：查询
        self.keyMap = {}

    def delete(self, node):

        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            if node.pre is self.freqMap[node.freq][0] and node.nex is self.frepMap[node.freq][-1]:
                self.freqMap.pop(node.freq)
            return node.key
        
    def increase(self, node):
        node.freq += 1
        self.delete(node)
        # 在尾部插入
        self.freqMap[node.freq][-1].pre.insert(node)
        # 新插入节点的频率
        if node.freq == 1:
            self.minFreq = 1
        # 节点频率为原最小频率
        elif self.minFreq == node.freq - 1:
            head, tail = self.freqMap[node.freq - 1]
            if head.nex is tail:
                self.minFreq = node.freq

    def get(self, key: int) -> int:
        if key in self.keyMap:
            self.increase(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.keyMap:
                node = self.keyMap[key]
                node.val = value
            else:
                node = Node(key, value)
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                # 删除最小评率的队头
                deleted = self.delete(self.freqMap[self.minFreq][0].nex)
                self.keyMap.pop(deleted)
            self.increase(node)




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)