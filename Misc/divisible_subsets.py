# Problem source: https://www.youtube.com/watch?v=bOXCLR3Wric
# find the number of subsets in {1, 2, ..., n} whose sum is divisible by k

# Solution: dynamic programming
# Time complexity: O(nk)
# Space complexity: O(k)
# not exactly because the answer will be huge
# the compute time and memory usage will depend on the size of the answer

def divisible_subsets(n: int, k: int) -> int:
    # prev[i]/curr[i] = number of subsets whose residual of sum mod k is i
    prev = [0] * k
    curr = [0] * k
    for i in range(1, n+1):
        curr[i % k] += 1
        for j in range(k):
            if prev[j] == 0:
                continue
            curr[(j + i) % k] += prev[j]
        prev = curr[:]
        # residual 1, 2, 3, ..., mod-1, 0
        # print(i, curr[1:]+[curr[0]])

    # plus 1 because the empty set is also a subset
    return curr[0]+1

if __name__ == '__main__':
    n = 2000
    k = 5
    ans = divisible_subsets(n, k)
    # compare with the answer we get from generation function
    assert ans == (2 ** 2000 + 4 * 2 ** 400) // 5
    print(ans)
