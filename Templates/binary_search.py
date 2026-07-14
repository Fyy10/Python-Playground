from typing import Callable


def bisect_left(left: int, right: int, val: int, func: Callable[[int], int]) -> int:
    """
    Find left-most position in the range [left, right) to insert val into [func(left), func(left+1), ..., func(right-1)] maintaining the sorted order.
    Assumes func to be monotonic non-decreasing.

    Args:
        left: left boundary (inclusive)
        right: right boundary (exclusive)
        val: int
        func: int -> int
    """
    while left < right:
        mid = (left + right) >> 1
        if val <= func(mid):
            right = mid
        else:
            left = mid + 1
    return left


def bisect_right(left: int, right: int, val: int, func: Callable[[int], int]) -> int:
    """
    Find right-most position in the range [left, right) to insert val into [func(left), func(left+1), ..., func(right-1)] maintaining the sorted order.
    Or rephrase as: find the insertion position after any existing entries of val in the range [left, right).
    Assumes func to be monotonic non-decreasing.

    Args:
        left: left boundary (inclusive)
        right: right boundary (exclusive)
        val: int
        func: int -> int
    """
    while left < right:
        mid = (left + right) >> 1
        if func(mid) <= val:
            left = mid + 1
        else:
            right = mid
    return right


if __name__ == '__main__':
    from bisect import bisect_left as std_bisect_left
    from bisect import bisect_right as std_bisect_right

    test_cases = [
        [],
        [1],
        [1, 1, 1],
        [1, 2, 3],
        [1, 2, 2, 2, 3],
        [-5, -3, -3, 0, 4, 9],
        [0, 10, 20, 30, 40, 50],
    ]
    test_values = [-10, -5, -3, -1, 0, 1, 2, 3, 4, 9, 10, 25, 50, 100]

    for arr in test_cases:
        for left in range(len(arr) + 1):
            for right in range(left, len(arr) + 1):
                sub_arr = arr[left:right]

                for val in test_values:

                    def func(i, a=arr):
                        return a[i]

                    actual_left = bisect_left(left, right, val, func)
                    expected_left = left + std_bisect_left(sub_arr, val)
                    assert actual_left == expected_left, (
                        f'bisect_left failed: arr={arr}, left={left}, right={right}, '
                        f'val={val}, actual={actual_left}, expected={expected_left}'
                    )

                    actual_right = bisect_right(left, right, val, func)
                    expected_right = left + std_bisect_right(sub_arr, val)
                    assert actual_right == expected_right, (
                        f'bisect_right failed: arr={arr}, left={left}, right={right}, '
                        f'val={val}, actual={actual_right}, expected={expected_right}'
                    )

                    assert left <= actual_left <= right
                    assert left <= actual_right <= right
                    assert actual_left <= actual_right

    # Explicit edge-case examples.
    assert bisect_left(0, 0, 10, lambda i: i) == 0
    assert bisect_right(0, 0, 10, lambda i: i) == 0
    assert bisect_left(3, 3, 10, lambda i: i) == 3
    assert bisect_right(3, 3, 10, lambda i: i) == 3

    arr = [1, 2, 2, 2, 3]
    assert bisect_left(0, len(arr), 2, lambda i: arr[i]) == 1
    assert bisect_right(0, len(arr), 2, lambda i: arr[i]) == 4
    assert bisect_left(1, 4, 2, lambda i: arr[i]) == 1
    assert bisect_right(1, 4, 2, lambda i: arr[i]) == 4

    print('All binary search tests passed.')
