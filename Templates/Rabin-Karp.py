def check(text: str, pattern: str, i: int, monte_carlo=True):
    if monte_carlo:
        # Monte Carlo Algorithm
        return True
    else:
        # Las Vegas Algorithm
        n = len(text)
        m = len(pattern)
        if i + m > n:
            return False
        return text[i:i+m] == pattern

def rk_search(text: str, pattern: str):
    """
    Rabin-Karp Algorithm
    """
    n = len(text)
    m = len(pattern)

    if n < m:
        return []

    # big prime number for hashing
    Q = 1e9 + 7

    # size of charset
    R = 256

    # R^m mod Q
    Rm = 1
    for i in range(m):
        Rm = (Rm * R) % Q

    # hash value of pattern
    hp = 0
    for i in range(m):
        hp = (hp * R + ord(pattern[i])) % Q

    # hash value of text[:m]
    ht = 0
    for i in range(m):
        ht = (ht * R + ord(text[i])) % Q

    ans = []
    if hp == ht and check(text, pattern, 0):
        ans.append(0)

    for i in range(1, n - m + 1):
        # add one additional Q to avoid negative value
        ht = (ht * R - ord(text[i-1]) * Rm + ord(text[i+m-1]) + Q) % Q
        if ht == hp and check(text, pattern, i):
            ans.append(i)

    return ans


if __name__ == '__main__':
    text = 'abcdabceabcdabcf'
    pattern = 'abcdabcf'
    print(rk_search(text, pattern))  # [8]

    text = 'defabcabc'
    pattern = 'abc'
    print(rk_search(text, pattern))  # [3, 6]

    text = 'aaaaaa'
    pattern = 'aa'
    print(rk_search(text, pattern))  # [0, 1, 2, 3, 4]

    text = 'aabaaabaaac'
    pattern = 'aabaaac'
    print(rk_search(text, pattern))  # [4]

    text = 'bbababaaaababbaabbbabbbaaabbbaaababbabaabbaaaaabbaaabbbbaaabaabbaababbbaabaaababbaaabbbbbbaabbbbbaaabbababaaaaabaabbbababbaababaabbaa'
    pattern = 'bbabba'
    print(rk_search(text, pattern))  # []

    text = 'aaaaa'
    pattern = 'bba'
    print(rk_search(text, pattern))  # []
