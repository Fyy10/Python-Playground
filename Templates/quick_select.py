import random

# Hoare's selection algorithm
def quick_select(nums, k):
    """
    select the k-th smallest element from nums
    """
    pivot = random.choice(nums)
    left, mid, right = [], [], []
    for num in nums:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            mid.append(num)
        else:
            right.append(num)

    # in the left portion
    if len(left) >= k:
        return quick_select(left, k)

    # in the right portion
    if len(left) + len(mid) < k:
        return quick_select(right, k - len(left) - len(mid))

    # in the mid portion
    return pivot


if __name__ == '__main__':
    arr = list(range(10))
    random.shuffle(arr)
    print(quick_select(arr, 5))
