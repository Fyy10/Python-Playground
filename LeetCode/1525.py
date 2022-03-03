class Solution:
    def numSplits(self, s: str) -> int:
        found = dict()
        left = []
        right = []

        cnt = 0
        for char in s:
            if found.get(char) == None:
                cnt += 1
                found[char] = 1
            left.append(cnt)
        
        cnt = 0
        found.clear()
        for char in reversed(s):
            if found.get(char) == None:
                cnt += 1
                found[char] = 1
            right.append(cnt)
        right.reverse()

        assert len(left) == len(right)

        ans = 0
        for idx, num in enumerate(left[:-1]):
            if num == right[idx + 1]:
                ans += 1

        return ans


sol = Solution()
num = sol.numSplits('aaaaaa')
print(num)
