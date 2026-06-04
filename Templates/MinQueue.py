# implementation with monotonic queue
from collections import deque


class MinQueue:
    def __init__(self):
        self.queue = deque()
        self.min_queue = deque()

    def append(self, val: int):
        self.queue.append(val)
        while self.min_queue and self.min_queue[-1] > val:
            self.min_queue.pop()
        self.min_queue.append(val)

    def popleft(self) -> int:
        if self.min_queue[0] == self.queue[0]:
            self.min_queue.popleft()
        return self.queue.popleft()

    def front(self) -> int:
        return self.queue[0]

    def end(self) -> int:
        return self.queue[-1]

    def min(self) -> int:
        return self.min_queue[0]


if __name__ == '__main__':

    def assert_state(q: MinQueue, expected: list[int]):
        assert list(q.queue) == expected
        assert q.front() == expected[0]
        assert q.end() == expected[-1]
        assert q.min() == min(expected)
        assert list(q.min_queue) == sorted(q.min_queue)

    def run_case(ops):
        q = MinQueue()
        expected = []
        for op in ops:
            if op == 'pop':
                q.popleft()
                expected.pop(0)
            else:
                q.append(op)
                expected.append(op)
            if expected:
                assert_state(q, expected)
            else:
                assert not q.queue
                assert not q.min_queue

    run_case([3, 1, 2, 'pop', 'pop', 2, -1, -1, 'pop', 'pop', 'pop', 'pop', 5])
    run_case([1, 2, 3, 4, 5, 'pop', 'pop', 'pop', 'pop', 'pop'])
    run_case([5, 4, 3, 2, 1, 'pop', 'pop', 'pop', 'pop', 'pop'])
    run_case([2, 2, 2, 1, 1, 3, 'pop', 'pop', 'pop', 'pop', 'pop', 'pop'])
    run_case([0, -5, 4, -5, 3, 'pop', 2, 'pop', 'pop', -6, 'pop', 'pop', 'pop'])

    q = MinQueue()
    expected = []
    for i in range(100):
        val = ((i * 37) % 23) - 11
        q.append(val)
        expected.append(val)
        assert_state(q, expected)

    for _ in range(100):
        q.popleft()
        expected.pop(0)
        if expected:
            assert_state(q, expected)
        else:
            assert not q.queue
            assert not q.min_queue
