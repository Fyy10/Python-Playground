from typing import Callable, List


class Node:
    def __init__(self, l: int, r: int, identity):
        self.l = l
        self.r = r
        self.left: 'Node|None' = None
        self.right: 'Node|None' = None
        self.val = identity


class SegmentTree:
    def __init__(self, nums: List[int], merge: Callable[[int, int], int], identity):
        if not nums:
            raise ValueError('The provided nums array is invalid:', nums)
        self.merge = merge
        self.identity = identity
        self.n = len(nums)
        self.root = self._build(nums, 0, self.n - 1)

    def _build(self, nums: List[int], l: int, r: int) -> Node:
        node = Node(l, r, self.identity)
        if l == r:
            node.val = nums[l]
            return node

        mid = (l + r) // 2
        node.left = self._build(nums, l, mid)
        node.right = self._build(nums, mid + 1, r)

        node.val = self.merge(node.left.val, node.right.val)

        return node

    def _query(self, node: Node, l: int, r: int):
        if node.l == l and node.r == r:
            return node.val
        mid = (node.l + node.r) // 2
        vl = vr = self.identity
        if r <= mid:
            vl = self._query(node.left, l, r)
        elif l > mid:
            vr = self._query(node.right, l, r)
        else:
            vl = self._query(node.left, l, mid)
            vr = self._query(node.right, mid + 1, r)

        return self.merge(vl, vr)

    def _update(self, node: Node, idx: int, val: int):
        if node.l == node.r:
            node.val = val
            return
        mid = (node.l + node.r) // 2
        if idx <= mid:
            self._update(node.left, idx, val)
        else:
            self._update(node.right, idx, val)

        node.val = self.merge(node.left.val, node.right.val)

    def query(self, l: int, r: int) -> int:
        if not 0 <= l <= r < self.n:
            raise ValueError(
                f'The queried range [{l}, {r}] is invalid or out of actual range [0, {self.n})'
            )
        return self._query(self.root, l, r)

    def update(self, idx: int, val: int):
        if not 0 <= idx < self.n:
            raise IndexError(f'The provided index {idx} is out of range [0, {self.n})')
        self._update(self.root, idx, val)


if __name__ == '__main__':

    def check(actual, expected, label):
        if actual != expected:
            raise AssertionError(f'{label}: expected {expected}, got {actual}')
        print(f'PASS: {label} = {actual}')

    def check_raises(fn, expected_exception, label):
        try:
            fn()
        except expected_exception as e:
            print(f'PASS: {label} raised {type(e).__name__}: {e}')
        except Exception as e:
            raise AssertionError(
                f'{label}: expected {expected_exception.__name__}, got {type(e).__name__}: {e}'
            )
        else:
            raise AssertionError(f'{label}: expected {expected_exception.__name__}')

    nums = [5, -2, 7, 3, 0, 9, -4]

    # sum test cases
    sum_tree = SegmentTree(nums, lambda a, b: a + b, 0)
    check(sum_tree.query(0, 6), 18, 'sum [0, 6]')
    check(sum_tree.query(1, 3), 8, 'sum [1, 3]')
    check(sum_tree.query(4, 4), 0, 'sum [4, 4]')

    sum_tree.update(1, 6)  # [5, 6, 7, 3, 0, 9, -4]
    check(sum_tree.query(0, 6), 26, 'sum after update idx 1 to 6')
    check(sum_tree.query(1, 3), 16, 'sum [1, 3] after update')

    sum_tree.update(6, 10)  # [5, 6, 7, 3, 0, 9, 10]
    check(sum_tree.query(3, 6), 22, 'sum [3, 6] after second update')

    # min test cases
    min_tree = SegmentTree(nums, min, float('inf'))
    check(min_tree.query(0, 6), -4, 'min [0, 6]')
    check(min_tree.query(0, 2), -2, 'min [0, 2]')
    check(min_tree.query(3, 5), 0, 'min [3, 5]')

    min_tree.update(6, 8)  # [5, -2, 7, 3, 0, 9, 8]
    check(min_tree.query(0, 6), -2, 'min after update idx 6 to 8')

    min_tree.update(1, 4)  # [5, 4, 7, 3, 0, 9, 8]
    check(min_tree.query(0, 6), 0, 'min after update idx 1 to 4')
    check(min_tree.query(0, 3), 3, 'min [0, 3] after updates')

    # max test cases
    max_tree = SegmentTree(nums, max, float('-inf'))
    check(max_tree.query(0, 6), 9, 'max [0, 6]')
    check(max_tree.query(0, 3), 7, 'max [0, 3]')
    check(max_tree.query(6, 6), -4, 'max [6, 6]')

    max_tree.update(2, -8)  # [5, -2, -8, 3, 0, 9, -4]
    check(max_tree.query(0, 3), 5, 'max [0, 3] after update idx 2 to -8')

    max_tree.update(4, 12)  # [5, -2, -8, 3, 12, 9, -4]
    check(max_tree.query(0, 6), 12, 'max after update idx 4 to 12')
    check(max_tree.query(4, 5), 12, 'max [4, 5] after updates')

    # exception test cases
    check_raises(
        lambda: SegmentTree([], lambda a, b: a + b, 0),
        ValueError,
        'empty nums',
    )

    error_tree = SegmentTree(nums, lambda a, b: a + b, 0)

    check_raises(lambda: error_tree.query(-1, 3), ValueError, 'query negative left')
    check_raises(lambda: error_tree.query(2, 7), ValueError, 'query right out of range')
    check_raises(
        lambda: error_tree.query(4, 3), ValueError, 'query left greater than right'
    )
    check_raises(lambda: error_tree.query(7, 7), ValueError, 'query left out of range')

    check_raises(
        lambda: error_tree.update(-1, 100), IndexError, 'update negative index'
    )
    check_raises(
        lambda: error_tree.update(7, 100), IndexError, 'update index out of range'
    )
