from threading import Lock
from typing import Callable


class ReaderWriter:
    def __init__(self):
        self.read_count = 0
        self.mutex = Lock()
        self.rw_mutex = Lock()

    def read(self, read_func: Callable):
        with self.mutex:
            self.read_count += 1
            if self.read_count == 1:
                self.rw_mutex.acquire()
        try:
            return read_func()
        finally:
            with self.mutex:
                self.read_count -= 1
                if self.read_count == 0:
                    self.rw_mutex.release()

    def write(self, write_func: Callable):
        with self.rw_mutex:
            write_func()


class FairReaderWriter:
    def __init__(self):
        self.read_count = 0
        self.rc_mutex = Lock()
        self.rw_mutex = Lock()
        self.gate = Lock()

    def read(self, read_func: Callable):
        with self.gate:
            with self.rc_mutex:
                self.read_count += 1
                if self.read_count == 1:
                    self.rw_mutex.acquire()
        try:
            return read_func()
        finally:
            with self.rc_mutex:
                self.read_count -= 1
                if self.read_count == 0:
                    self.rw_mutex.release()

    def write(self, write_func: Callable):
        with self.gate:
            with self.rw_mutex:
                write_func()
