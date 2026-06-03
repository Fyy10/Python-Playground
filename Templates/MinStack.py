# implementation with additional min stack
class MinStack1:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


# implementation with diff notation
class MinStack2:
    def __init__(self):
        self.stack = []
        self.min_val = 0

    def push(self, val: int):
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            self.stack.append(val - self.min_val)
            if val < self.min_val:
                self.min_val = val

    def pop(self):
        if self.stack[-1] < 0:
            self.min_val -= self.stack[-1]
        self.stack.pop()

    def top(self) -> int:
        if self.stack[-1] >= 0:
            return self.stack[-1] + self.min_val
        else:
            return self.min_val

    def min(self) -> int:
        return self.min_val
