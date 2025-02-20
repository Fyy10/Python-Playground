from collections import defaultdict


def bm_search(text: str, pattern: str):
    """
    Boyer-Moore Algorithm

    v1.0: bad character rule with 1D array
    """
    n = len(text)
    m = len(pattern)

    # right[c] is the rightmost position of c in pattern
    # if c is not in pattern, right[c] = -1
    right = defaultdict(lambda: -1)
    for i, c in enumerate(pattern):
        right[c] = i

    ans = []
    i = 0
    while i <= n - m:
        skip = 0
        # j from m-1 to 0
        for j in range(m-1, -1, -1):
            if text[i+j] != pattern[j]:
                # if text[i+j] not in pattern: move i forward j+1 steps (equals j - right[text[i+j]])
                # if text[i+j] is in pattern: move i forward j - right[text[i+j]] steps
                # j - right[c] means how many steps needed to move c forward to match j's position
                skip = j - right[text[i+j]]
                # skip will never be 0 here
                assert skip != 0
                if skip < 0:
                    skip = 1
                break

        if skip == 0:
            ans.append(i)
            skip = 1

        i += skip

    return ans


if __name__ == '__main__':
    text = 'abcdabceabcdabcf'
    pattern = 'abcdabcf'
    print(bm_search(text, pattern))  # [8]

    text = 'defabcabc'
    pattern = 'abc'
    print(bm_search(text, pattern))  # [3, 6]

    text = 'aaaaaa'
    pattern = 'aa'
    print(bm_search(text, pattern))  # [0, 1, 2, 3, 4]

    text = 'aabaaabaaac'
    pattern = 'aabaaac'
    print(bm_search(text, pattern))  # [4]

    text = 'bbababaaaababbaabbbabbbaaabbbaaababbabaabbaaaaabbaaabbbbaaabaabbaababbbaabaaababbaaabbbbbbaabbbbbaaabbababaaaaabaabbbababbaababaabbaa'
    pattern = 'bbabba'
    print(bm_search(text, pattern))  # []

    text = 'aaaaa'
    pattern = 'bba'
    print(bm_search(text, pattern))  # []
