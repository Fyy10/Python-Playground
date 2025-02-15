def kmp_search(text: str, pattern: str):
    n = len(text)
    m = len(pattern)

    nxt = [0]
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = nxt[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        nxt.append(j)

    j = 0
    ans = []
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = nxt[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            ans.append(i - m + 1)
            j = nxt[j - 1]

    return ans


if __name__ == '__main__':
    text = 'abcdabceabcdabcf'
    pattern = 'abcdabcf'
    print(kmp_search(text, pattern))  # [8]

    text = 'defabcabc'
    pattern = 'abc'
    print(kmp_search(text, pattern))  # [3, 6]

    text = 'aaaaaa'
    pattern = 'aa'
    print(kmp_search(text, pattern))  # [0, 1, 2, 3, 4]

    text = 'aabaaabaaac'
    pattern = 'aabaaac'
    print(kmp_search(text, pattern))  # [4]

    text = 'bbababaaaababbaabbbabbbaaabbbaaababbabaabbaaaaabbaaabbbbaaabaabbaababbbaabaaababbaaabbbbbbaabbbbbaaabbababaaaaabaabbbababbaababaabbaa'
    pattern = 'bbabba'
    print(kmp_search(text, pattern))  # []
