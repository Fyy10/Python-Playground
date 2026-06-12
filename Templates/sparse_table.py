from math import floor, gcd, log2
from typing import Callable, List


class SparseTable:
    def __init__(self, arr: List[int], func: Callable[[int, int], int]):
        """
        Build a sparse table over arr using func as the range-combine operation.

        st[i][j] stores the result of applying func to the interval that starts
        at index i and has length 2**j.

        query() answers a range in O(1) by combining two possibly overlapping
        blocks, so it is valid only for idempotent operations such as min, max,
        or gcd. query_non_overlap() answers a range in O(log N) by combining
        disjoint blocks from left to right, so it also supports non-idempotent
        associative operations such as sum or product.
        """
        self.n = len(arr)
        self.log = [0] + [floor(log2(i)) for i in range(1, self.n + 1)]
        self.func = func
        self.st = [[arr[i]] for i in range(self.n)]

        for i in range(self.n - 1, -1, -1):
            for j in range(1, self.log[self.n - i] + 1):
                self.st[i].append(
                    self.func(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])
                )

    def _check_range(self, l: int, r: int):
        if l < 0 or r >= self.n or l > r:
            raise IndexError(
                f'The queried range [{l}, {r}] is invalid or out of actual range [0, {self.n})'
            )

    def query(self, l: int, r: int) -> int:
        self._check_range(l, r)
        s = self.log[r - l + 1]
        return self.func(self.st[l][s], self.st[r - (1 << s) + 1][s])

    def query_non_overlap(self, l: int, r: int) -> int:
        self._check_range(l, r)

        res: int | None = None
        while l <= r:
            s = self.log[r - l + 1]
            if res is None:
                res = self.st[l][s]
            else:
                res = self.func(res, self.st[l][s])
            l += 1 << s
        return res


if __name__ == '__main__':

    def assert_raises(error_type, fn):
        try:
            fn()
        except error_type:
            return
        raise AssertionError(f'Expected {error_type.__name__} to be raised')

    arr = [5, 2, 4, 7, 1, 3, 6, 0]

    # Range minimum queries.
    min_st = SparseTable(arr, min)
    assert min_st.query(0, 0) == 5
    assert min_st.query(4, 4) == 1
    assert min_st.query(0, 7) == 0
    assert min_st.query(1, 3) == 2
    assert min_st.query(2, 5) == 1
    assert min_st.query(5, 6) == 3

    # Range maximum queries.
    max_st = SparseTable(arr, max)
    assert max_st.query(0, 0) == 5
    assert max_st.query(0, 7) == 7
    assert max_st.query(1, 2) == 4
    assert max_st.query(3, 6) == 7
    assert max_st.query(5, 7) == 6

    # GCD is also idempotent, so overlapping query blocks are safe.
    gcd_arr = [24, 36, 48, 18, 30, 42]
    gcd_st = SparseTable(gcd_arr, gcd)
    assert gcd_st.query(0, 0) == 24
    assert gcd_st.query(0, 2) == 12
    assert gcd_st.query(1, 4) == 6
    assert gcd_st.query(3, 5) == 6
    assert gcd_st.query(0, 5) == 6

    # Invalid ranges.
    assert_raises(IndexError, lambda: min_st.query(-1, 2))
    assert_raises(IndexError, lambda: min_st.query(2, 8))
    assert_raises(IndexError, lambda: min_st.query(4, 3))
    assert_raises(IndexError, lambda: SparseTable([], min).query(0, 0))

    # This implementation is not valid for non-idempotent operations like sum.
    sum_st = SparseTable([1, 2, 3], lambda a, b: a + b)
    assert sum_st.query(0, 2) != 6

    # Non-overlapping queries decompose the interval into left-to-right blocks.
    sum_arr = list(range(1, 14))
    sum_st = SparseTable(sum_arr, lambda a, b: a + b)
    assert sum_st.query_non_overlap(0, 0) == 1
    assert sum_st.query_non_overlap(0, 4) == 15
    assert sum_st.query_non_overlap(3, 7) == 30
    assert sum_st.query_non_overlap(0, 12) == 91
    assert sum_st.query_non_overlap(5, 12) == 76

    product_st = SparseTable([2, 3, 5, 7, 11, 13], lambda a, b: a * b)
    assert product_st.query_non_overlap(0, 2) == 30
    assert product_st.query_non_overlap(1, 4) == 1155
    assert product_st.query_non_overlap(0, 5) == 30030

    assert_raises(IndexError, lambda: sum_st.query_non_overlap(-1, 2))
    assert_raises(IndexError, lambda: sum_st.query_non_overlap(2, 13))
    assert_raises(IndexError, lambda: sum_st.query_non_overlap(4, 3))

    print('All sparse table test cases passed.')
