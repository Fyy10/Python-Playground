from collections import deque
from threading import Condition, Lock, Semaphore


class CondBoundedQueue:
    def __init__(self, cap: int):
        self.cap = cap
        self.q = deque()
        self.lock = Lock()
        self.cond_not_full = Condition(self.lock)
        self.cond_not_empty = Condition(self.lock)

    def put(self, elem: int):
        with self.lock:
            while len(self.q) == self.cap:
                self.cond_not_full.wait()
            self.q.append(elem)
            self.cond_not_empty.notify()

    def get(self) -> int:
        with self.lock:
            while len(self.q) == 0:
                self.cond_not_empty.wait()
            res = self.q.popleft()
            self.cond_not_full.notify()
            return res

    def size(self) -> int:
        with self.lock:
            return len(self.q)


class SemBoundedQueue:
    def __init__(self, cap: int):
        self.cap = cap
        self.q = deque()
        self.empty = Semaphore(cap)
        self.full = Semaphore(0)
        self.mutex = Lock()

    def put(self, elem: int):
        self.empty.acquire()
        with self.mutex:
            self.q.append(elem)
        self.full.release()

    def get(self) -> int:
        self.full.acquire()
        with self.mutex:
            ret = self.q.popleft()
        self.empty.release()
        return ret

    def size(self) -> int:
        with self.mutex:
            return len(self.q)
