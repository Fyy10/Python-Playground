import random


def convert_base(n: int, d: int):
    """
    Convert base 10 number n to base d number (d <= 16)
    """
    assert d <= 16

    digits = []
    while n:
        digit = n % d
        n //= d
        if digit < 10:
            digits.append(chr(ord('0') + digit))
        else:
            digits.append(chr(ord('A') + digit - 10))

    return ''.join(reversed(digits))


def restore(num: str, d: int):
    """
    Convert base d number num to base 10 (d <= 16)
    """
    assert d <= 16

    ans = 0
    for c in num:
        digit = 0
        if ord('0') <= ord(c) <= ord('9'):
            digit = ord(c) - ord('0')
        elif ord('A') <= ord(c) <= ord('F'):
            digit = ord(c) - ord('A') + 10
        elif ord('a') <= ord(c) <= ord('f'):
            digit = ord(c) - ord('a') + 10
        else:
            raise ValueError(f'Invalid character "{c}"')

        if digit >= d:
            raise ValueError(f'"{c}" is not a valid digit for base {d} number {num}')

        ans = ans * d + digit

    return ans


if __name__ == '__main__':
    t = 1000
    for _ in range(t):
        n = random.randint(0, 100000000)
        d = random.randint(2, 16)
        assert n == restore(convert_base(n, d), d)
