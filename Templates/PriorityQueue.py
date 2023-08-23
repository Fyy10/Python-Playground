import heapq

class PriorityQueue:
    def __init__(self, lst=[]):
        self._queue = lst
        heapq.heapify(self._queue)

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return str(self._queue)

    def size(self):
        return len(self._queue)

    def empty(self):
        return len(self._queue) == 0

    def clear(self):
        self._queue = []

    def __getitem__(self, idx):
        if not 0 <= idx < len(self._queue):
            raise IndexError('index out of range')
        return self._queue[idx]

    def top(self):
        return self._queue[0]

    def push(self, item):
        heapq.heappush(self._queue, item)

    def pop(self):
        return heapq.heappop(self._queue)


if __name__ == '__main__':
    pq = PriorityQueue([5, 1, 3, -2, 2])
    print(pq)
    pq.push(4)
    print(pq)
    while pq:
        print(pq.pop())

    pq.clear()
    pq.push((5, 'a'))
    pq.push((3, 'b'))
    pq.push((7, 'c'))
    while pq:
        print(pq.pop())
