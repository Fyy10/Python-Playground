class Node:
    def __init__(
        self, key: int, val: int, prev: 'Node|None' = None, nxt: 'Node|None' = None
    ):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class DoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def append(self, x: Node):
        if not self.tail:
            self.head = self.tail = x
        else:
            self.tail.nxt = x
            x.prev = self.tail
            self.tail = x
            self.tail.nxt = None

    def append_left(self, x: Node):
        if not self.head:
            self.head = self.tail = x
        else:
            x.nxt = self.head
            self.head.prev = x
            self.head = x
            self.head.prev = None

    def remove(self, x: Node):
        if x == self.head and x == self.tail:
            self.head = self.tail = None
        elif x == self.head:
            self.head = self.head.nxt
            self.head.prev = None
        elif x == self.tail:
            self.tail = self.tail.prev
            self.tail.nxt = None
        else:
            x.prev.nxt = x.nxt
            x.nxt.prev = x.prev

    def pop(self) -> Node:
        ret = self.tail
        self.remove(self.tail)
        return ret

    def pop_left(self) -> Node:
        ret = self.head
        self.remove(self.head)
        return ret


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.dict: dict[int, Node] = {}
        self.list = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.list.remove(node)
            self.list.append(node)
            return node.val
        else:
            return -1

    def put(self, key: int, val: int):
        if key in self.dict:
            node = self.dict[key]
            node.val = val
            self.list.remove(node)
            self.list.append(node)
        else:
            node = Node(key, val)
            self.dict[key] = node
            self.list.append(node)
            self.size += 1

            if self.size > self.cap:
                evict_node = self.list.pop_left()
                self.dict.pop(evict_node.key)
                self.size -= 1


if __name__ == '__main__':
    cache = LRUCache(1)
    cache.put(1, 2)
    print(cache.get(1))  # 2
    print(cache.get(2))  # -1
    cache.put(2, 3)
    print(cache.get(2))  # 3
    print(cache.get(1))  # -1

    cache = LRUCache(2)
    cache.put(1, 2)
    cache.put(2, 3)
    cache.get(1)
    cache.put(3, 4)
    print(cache.get(2))  # -1
